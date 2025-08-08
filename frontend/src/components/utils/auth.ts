export function getToken(): string | null {
  return localStorage.getItem("token") || sessionStorage.getItem("token");
}

export function isTokenValid(token: string | null): boolean {
  if (!token) return false;
  try {
    const [, payload] = token.split(".");
    const decoded = JSON.parse(atob(payload));
    const exp = decoded.exp;
    return exp * 1000 > Date.now(); // JWT expiration is in seconds
  } catch (e) {
    return false;
  }
}
