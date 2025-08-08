export async function loginUser(email: string, password: string): Promise<boolean> {
  try {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      return false;
    }

    const data = await response.json();

    // Guardar token e role no localStorage
    localStorage.setItem("token", data.token);
    if (data.role) {
      localStorage.setItem("role", data.role);
    }

    return true;
  } catch (error) {
    console.error("Erro na autenticação:", error);
    return false;
  }
}

export async function verifyTotp(code: string): Promise<boolean> {
  try {
    const token = localStorage.getItem("token");
    if (!token) return false;

    const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/verify-totp`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({ code }),
    });

    if (!response.ok) {
      return false;
    }

    const data = await response.json();

    // Substituir token antigo por novo token validado após TOTP
    localStorage.setItem("token", data.token);
    return true;
  } catch (error) {
    console.error("Erro na verificação TOTP:", error);
    return false;
  }
}