'use client';

import { useEffect, useRef, useState } from 'react';
import { RotateCcw, Trophy } from 'lucide-react';

type Point = { x: number; y: number };
type Guess = Point & { score: number };

export default function PlayCorner() {
  const canvas = useRef<HTMLCanvasElement>(null);
  const [target, setTarget] = useState<Point>({ x: 0.5, y: 0.5 });
  const [ready, setReady] = useState(false);
  const [guesses, setGuesses] = useState<Guess[]>([]);
  const [best, setBest] = useState<number | null>(null);
  const finished = guesses.length === 5;
  const score = guesses.length ? Math.max(...guesses.map(guess => guess.score)) : 0;

  function newRound() {
    setTarget({ x: 0.18 + Math.random() * 0.64, y: 0.18 + Math.random() * 0.64 });
    setGuesses([]);
    setReady(true);
  }

  useEffect(() => {
    setTarget({ x: 0.18 + Math.random() * 0.64, y: 0.18 + Math.random() * 0.64 });
    setReady(true);
    try {
      const stored = localStorage.getItem('optimization-personal-best');
      const value = Number(stored);
      if (stored && Number.isFinite(value) && value >= 0 && value <= 100) setBest(value);
    } catch { /* The game also works without browser storage. */ }
  }, []);

  useEffect(() => {
    const element = canvas.current;
    const ctx = element?.getContext('2d');
    if (!element || !ctx) return;
    ctx.fillStyle = '#f7faf9';
    ctx.fillRect(0, 0, 720, 440);
    ctx.strokeStyle = '#dce6e1';
    ctx.lineWidth = 1;
    for (let x = 0; x <= 720; x += 40) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 440); ctx.stroke(); }
    for (let y = 0; y <= 440; y += 40) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(720, y); ctx.stroke(); }
    guesses.forEach((guess, index) => {
      ctx.beginPath(); ctx.arc(guess.x * 720, guess.y * 440, 13, 0, Math.PI * 2);
      ctx.fillStyle = '#247e70'; ctx.fill();
      ctx.fillStyle = '#ffffff'; ctx.font = 'bold 14px sans-serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(String(index + 1), guess.x * 720, guess.y * 440);
    });
    if (finished) {
      ctx.strokeStyle = '#e24f72'; ctx.lineWidth = 2;
      for (let r = 25; r < 360; r += 45) { ctx.beginPath(); ctx.ellipse(target.x * 720, target.y * 440, r * 720 / 440, r, 0, 0, Math.PI * 2); ctx.stroke(); }
      ctx.fillStyle = '#e24f72'; ctx.beginPath(); ctx.arc(target.x * 720, target.y * 440, 6, 0, Math.PI * 2); ctx.fill();
    }
  }, [guesses, target, finished]);

  function guess(point: Point) {
    if (!ready || finished) return;
    const distance = Math.hypot(point.x - target.x, point.y - target.y);
    const nextScore = Math.max(0, Math.round(100 * (1 - distance / Math.SQRT2)));
    setGuesses(current => [...current, { ...point, score: nextScore }]);
    if (guesses.length === 4) {
      const nextBest = Math.max(best ?? 0, score, nextScore);
      setBest(nextBest);
      try { localStorage.setItem('optimization-personal-best', String(nextBest)); } catch { /* Optional persistence. */ }
    }
  }

  return (
    <section className="border-t border-neutral-200 pt-8" id="play">
      <h2 className="text-2xl font-serif font-bold text-primary mb-5">Mini optimization game</h2>
      <div className="flex items-center justify-between gap-3 mb-3">
        <h3 className="font-medium">Find the hidden minimum</h3>
        <button type="button" onClick={newRound} title="New round" aria-label="New round" className="h-10 w-10 rounded-md flex items-center justify-center hover:bg-neutral-100"><RotateCcw size={18} /></button>
      </div>
      <div className="flex flex-wrap gap-x-5 gap-y-2 text-sm mb-3 text-neutral-500">
        <span>{guesses.length} / 5 attempts</span><span>Closest: {score} / 100</span>
        {best !== null && <span className="inline-flex items-center gap-1"><Trophy size={14} />Personal best: {best}</span>}
      </div>
      <canvas ref={canvas} width={720} height={440} tabIndex={0} role="button" aria-label="Search for the hidden minimum. Click or tap to guess. Press Enter to guess the center." aria-disabled={!ready || finished} onKeyDown={event => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); guess({ x: 0.5, y: 0.5 }); } }} onClick={event => { const rect = event.currentTarget.getBoundingClientRect(); guess({ x: Math.max(0, Math.min(1, (event.clientX - rect.left) / rect.width)), y: Math.max(0, Math.min(1, (event.clientY - rect.top) / rect.height)) }); }} className="block w-full aspect-[18/11] rounded-lg border border-neutral-300 cursor-crosshair focus-visible:outline-2 focus-visible:outline-accent" />
      <p aria-live="polite" className="mt-3 min-h-6 text-sm text-neutral-500">{finished ? `Round complete: ${score}/100. The pink dot reveals the minimum.` : guesses.length ? `Last attempt: ${guesses[guesses.length - 1].score}/100. ${guesses.length > 1 ? guesses[guesses.length - 1].score > guesses[guesses.length - 2].score ? 'Warmer!' : 'Colder.' : 'The closer you get, the higher your score.'}` : 'Five attempts. One hidden minimum.'}</p>
    </section>
  );
}
