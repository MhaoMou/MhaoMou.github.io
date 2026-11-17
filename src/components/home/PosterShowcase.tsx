'use client';

import { useRef } from 'react';
import Image from 'next/image';
import { Expand, ArrowUpRight, Download, X } from 'lucide-react';

const poster = {
  title: 'Who Gets Connected?',
  subtitle: 'A Classroom Game for Large-Load Interconnection',
  preview: '/posters/who-gets-connected.png',
  pdf: '/posters/who-gets-connected.pdf',
};

export default function PosterShowcase() {
  const dialog = useRef<HTMLDialogElement>(null);
  return (
    <section id="posters" aria-labelledby="posters-title" className="scroll-mt-24 border-t border-neutral-200 pt-8 dark:border-neutral-800">
      <div className="mb-5 flex items-baseline justify-between gap-4">
        <h2 id="posters-title" className="text-2xl font-serif font-bold text-primary">Posters</h2>
        <span className="text-xs text-neutral-500">Research in presentation</span>
      </div>
      <article>
        <button type="button" onClick={() => dialog.current?.showModal()} aria-label={`Enlarge poster: ${poster.title}`} className="group relative block w-full overflow-hidden rounded-md border border-neutral-200 bg-neutral-100 p-4 sm:p-7 dark:border-neutral-700 dark:bg-neutral-900 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-accent">
          <Image src={poster.preview} width={2000} height={1500} alt={`${poster.title} ${poster.subtitle}, by Minghao Mou and Junjie Qin`} className="h-auto w-full shadow-lg transition-transform duration-200 group-hover:scale-[1.01] motion-reduce:transition-none" sizes="(max-width: 1024px) 100vw, 680px" />
          <span className="absolute bottom-2 right-2 flex h-9 w-9 items-center justify-center rounded bg-background text-primary shadow" title="Enlarge poster"><Expand size={17} /></span>
        </button>
        <div className="mt-5 border-l-2 border-accent pl-4">
          <p className="mb-2 text-xs font-medium uppercase text-neutral-500">Presented poster · Purdue ECE</p>
          <h3 className="text-xl font-serif font-bold text-primary">{poster.title}</h3>
          <p className="mt-1 text-base text-primary">{poster.subtitle}</p>
          <p className="mt-2 text-sm text-neutral-500">Minghao Mou &amp; Junjie Qin</p>
          <p className="mt-3 text-sm leading-relaxed text-neutral-600 dark:text-neutral-400">A classroom game exploring how large loads connect to a constrained power grid, and how siting, generation, and allocation rules shape who gets served.</p>
          <div className="mt-4 flex flex-wrap gap-x-6 gap-y-3 text-sm font-medium text-accent">
            <a href={poster.pdf} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 underline-offset-4 hover:underline">View PDF <ArrowUpRight size={16} /></a>
            <a href={poster.pdf} download className="inline-flex items-center gap-1 underline-offset-4 hover:underline"><Download size={15} /> Download</a>
          </div>
        </div>
      </article>
      <dialog ref={dialog} aria-label={poster.title} onClick={(event) => { if (event.target === event.currentTarget) dialog.current?.close(); }} className="fixed inset-0 m-auto max-h-[94dvh] w-[96vw] max-w-[1600px] overflow-hidden rounded-lg border border-neutral-300 bg-background p-0 text-primary shadow-xl backdrop:bg-black/70">
        <div className="flex items-center justify-between gap-4 border-b border-neutral-200 px-4 py-3">
          <h3 className="min-w-0 text-sm font-semibold">{poster.title}</h3>
          <form method="dialog"><button aria-label="Close poster preview" title="Close" className="flex h-10 w-10 items-center justify-center rounded hover:bg-neutral-100 dark:hover:bg-neutral-800"><X size={20} /></button></form>
        </div>
        <div className="max-h-[calc(94dvh-66px)] overflow-auto p-3 sm:p-6">
          <Image src={poster.preview} width={2000} height={1500} alt={`${poster.title}: full poster`} className="h-auto min-w-[950px] w-full" sizes="1600px" />
        </div>
      </dialog>
    </section>
  );
}
