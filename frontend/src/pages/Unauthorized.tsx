import { useNavigate } from "react-router-dom";
import { Button } from "../components/ui/button";
import { motion } from "framer-motion";

const translations = {
  pt: {
    title: "Acesso não autorizado",
    message: "Não tem permissões para aceder a esta página.",
    back: "Voltar ao início",
  },
  en: {
    title: "Unauthorized Access",
    message: "You do not have permission to access this page.",
    back: "Return to Home",
  },
};

export default function Unauthorized() {
  const navigate = useNavigate();
  const lang = navigator.language.startsWith("pt") ? "pt" : "en";
  const t = translations[lang];

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="flex h-screen flex-col items-center justify-center bg-background px-4 text-center"
    >
      <h1 className="text-3xl font-bold mb-4">{t.title}</h1>
      <p className="text-muted-foreground mb-6">{t.message}</p>
      <Button onClick={() => navigate("/login")}>{t.back}</Button>
    </motion.div>
  );
}