import { useState } from "react";
import { motion } from "framer-motion";
import { Card, CardContent } from "../components/ui/card";
import { Input } from "../components/ui/input";
import { Button } from "../components/ui/button";
import { useNavigate } from "react-router-dom";

const translations = {
  pt: {
    title: "Recuperar Palavra-passe",
    emailPlaceholder: "Introduza o seu email",
    submitButton: "Enviar pedido",
    confirmation: "Se o email existir, receberá instruções brevemente.",
    error: "Ocorreu um erro. Por favor, tente novamente mais tarde.",
    backButton: "Voltar",
  },
  en: {
    title: "Recover Password",
    emailPlaceholder: "Enter your email",
    submitButton: "Send Request",
    confirmation: "If the email exists, you'll receive instructions shortly.",
    error: "An error occurred. Please try again later.",
    backButton: "Back",
  },
};

export default function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState("");
  const lang = typeof navigator !== "undefined" && navigator.language.startsWith("pt") ? "pt" : "en";
  const t = translations[lang];
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/auth/forgot-password`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email }),
      });
      if (!response.ok) {
        setError(t.error);
        return;
      }
      setSubmitted(true);
    } catch (error) {
      setError(t.error);
      console.error("Erro ao enviar pedido de recuperação:", error);
    }
  };

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-br from-blue-50 to-white px-6 py-12">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: "easeOut" }}
        className="mb-8 flex items-center space-x-3 cursor-pointer"
        onClick={() => navigate(-1)}
        aria-label={t.backButton}
        role="button"
        tabIndex={0}
        onKeyDown={(e: { key: string; }) => { if (e.key === 'Enter' || e.key === ' ') navigate(-1); }}
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-6 w-6 text-blue-600 hover:text-blue-800 transition-colors"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          strokeWidth={2}
          aria-hidden="true"
        >
          <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
        </svg>
        <span className="text-blue-600 font-medium hover:underline">{t.backButton}</span>
      </motion.div>

      <motion.div
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ duration: 0.5, ease: "easeOut" }}
        className="w-full max-w-md"
      >
        <div className="flex justify-center mb-6">
          <img
            src="/logo.svg"
            alt="Platform Logo"
            className="h-14 w-auto"
            draggable={false}
          />
        </div>
        <Card className="shadow-lg rounded-lg border border-gray-200">
          <CardContent className="py-12 px-8">
            <h1 className="text-3xl font-extrabold text-center text-gray-900 mb-8">{t.title}</h1>
            {submitted ? (
              <p className="text-center text-green-700 text-lg font-semibold">{t.confirmation}</p>
            ) : (
              <>
                <form onSubmit={handleSubmit} className="space-y-6">
                  <Input
                    type="email"
                    placeholder={t.emailPlaceholder}
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    autoFocus
                    className="text-lg"
                    aria-label={t.emailPlaceholder}
                  />
                  <Button type="submit" className="w-full py-3 text-lg font-semibold">
                    {t.submitButton}
                  </Button>
                </form>
                {error && !submitted && (
                  <p
                    className="text-center text-red-600 text-sm mt-4"
                    role="alert"
                    aria-live="assertive"
                  >
                    {error}
                  </p>
                )}
              </>
            )}
          </CardContent>
        </Card>
      </motion.div>
    </div>
  );
}