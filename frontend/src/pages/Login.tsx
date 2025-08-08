import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { loginUser, verifyTotp } from '../services/api';
import { Card, CardContent } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Button } from '../components/ui/button';
import { Checkbox } from '../components/ui/checkbox';
import { motion } from 'framer-motion';

const translations = {
  pt: {
    loginTitle: 'Iniciar Sessão',
    emailPlaceholder: 'Email',
    passwordPlaceholder: 'Palavra-passe',
    continueButton: 'Continuar',
    totpPlaceholder: 'Código 2FA',
    verifyButton: 'Verificar e Entrar',
    error2FARequired: 'A autenticação requer 2FA',
    errorAuth: 'Erro ao autenticar.',
    errorTotp: 'Código 2FA inválido.',
    rememberMeLabel: 'Lembrar-me',
    errorInvalidEmail: 'Email inválido.',
    forgotPasswordText: 'Esqueceu a palavra-passe?',
  },
  en: {
    loginTitle: 'Sign In',
    emailPlaceholder: 'Email',
    passwordPlaceholder: 'Password',
    continueButton: 'Continue',
    totpPlaceholder: '2FA Code',
    verifyButton: 'Verify and Enter',
    error2FARequired: 'Authentication requires 2FA',
    errorAuth: 'Authentication error.',
    errorTotp: 'Invalid 2FA code.',
    rememberMeLabel: 'Remember me',
    errorInvalidEmail: 'Invalid email.',
    forgotPasswordText: 'Forgot your password?',
  },
};

const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [totp, setTotp] = useState('');
  const [step, setStep] = useState<'credentials' | 'totp'>('credentials');
  const [error, setError] = useState('');
  const [lang, setLang] = useState<'pt' | 'en'>('pt');
  const [rememberMe, setRememberMe] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const t = translations[lang];

  const isValidEmail = (email: string) =>
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (!isValidEmail(email)) {
      setError(t.errorInvalidEmail);
      return;
    }

    setLoading(true);
    try {
      const success = await loginUser(email, password);
      if (success) {
        setStep('totp');
      } else {
        setError(t.errorAuth);
      }
    } catch (err: any) {
      setError(t.errorAuth);
    } finally {
      setLoading(false);
    }
  };

  const handleVerifyTotp = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      const token = await verifyTotp(totp);
      if (token) {
        if (rememberMe) {
          localStorage.setItem('token', String(token));
        } else {
          sessionStorage.setItem('token', String(token));
        }
        navigate('/dashboard');
      } else {
        setError(t.errorTotp);
      }
    } catch (err: any) {
      setError(t.errorTotp);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-gray-50">
        <Card className="w-full max-w-md p-6 shadow-lg">
          <CardContent>
            <p className="text-center text-lg font-medium text-gray-700">A carregar...</p>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gray-50 px-4">
      <div className="w-full max-w-md">
        <div className="flex justify-end mb-4">
          <select
            value={lang}
            onChange={(e) => setLang(e.target.value as 'pt' | 'en')}
            className="rounded-md border border-gray-300 bg-white py-1 px-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="pt">PT</option>
            <option value="en">EN</option>
          </select>
        </div>
        <div className="flex justify-center mb-6">
          <img
            src="/LOGO.jpeg"
            alt="DiBrand Logo"
            className="h-16 w-auto object-contain"
          />
        </div>
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <Card className="shadow-lg">
            <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.3, duration: 0.5 }}>
              <CardContent>
                <h2 className="mb-6 text-center text-2xl font-semibold text-gray-900">{t.loginTitle}</h2>
                {step === 'credentials' ? (
                  <form onSubmit={handleLogin} className="space-y-4">
                    <Input
                      type="email"
                      placeholder={t.emailPlaceholder}
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      required
                      autoComplete="email"
                    />
                    <Input
                      type="password"
                      placeholder={t.passwordPlaceholder}
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      required
                      autoComplete="current-password"
                    />
                    <div className="flex items-center space-x-2">
                      <Checkbox
                        id="rememberMe"
                        checked={rememberMe}
                        onCheckedChange={(checked: boolean | "indeterminate") => setRememberMe(checked === true)}
                      />
                      <label htmlFor="rememberMe" className="text-sm font-medium text-gray-700 cursor-pointer">
                        {t.rememberMeLabel}
                      </label>
                    </div>
                    <Button type="submit" className="w-full" disabled={loading}>
                      {t.continueButton}
                    </Button>
                    <p className="mt-2 text-center text-sm text-blue-600 hover:underline cursor-pointer">
                      <a href="/forgot-password">{t.forgotPasswordText}</a>
                    </p>
                  </form>
                ) : (
                  <form onSubmit={handleVerifyTotp} className="space-y-4">
                    <Input
                      type="text"
                      placeholder={t.totpPlaceholder}
                      value={totp}
                      onChange={(e) => setTotp(e.target.value)}
                      required
                      inputMode="numeric"
                      pattern="\d*"
                      maxLength={6}
                    />
                    <Button type="submit" className="w-full" disabled={loading}>
                      {t.verifyButton}
                    </Button>
                  </form>
                )}
                {error && (
                  <p className="mt-4 text-center text-sm text-red-600" role="alert">
                    {error}
                  </p>
                )}
              </CardContent>
            </motion.div>
          </Card>
        </motion.div>
      </div>
    </div>
  );
};

export default Login;