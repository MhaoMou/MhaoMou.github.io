'use client';

export default function CvPage() {
  return (
    <main className="space-y-6">
      <header className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="text-sm font-medium uppercase tracking-[0.16em] text-neutral-500">Curriculum vitae</p>
          <h1 className="mt-2 text-3xl font-serif font-bold text-primary">CV</h1>
          <p className="mt-2 text-sm text-neutral-600">View the current CV below, or download a copy for offline reading.</p>
        </div>
        <div className="flex flex-wrap gap-3">
          <a
            href="/cv.pdf"
            download="Minghao_Mou_CV.pdf"
            className="rounded-md border border-neutral-300 px-4 py-2 text-sm font-medium text-primary transition hover:border-accent hover:text-accent focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
          >
            Download PDF
          </a>
          <a
            href="/cv.pdf"
            target="_blank"
            rel="noreferrer"
            className="rounded-md bg-primary px-4 py-2 text-sm font-medium text-white transition hover:bg-accent focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
          >
            Open in new tab
          </a>
        </div>
      </header>

      <div className="overflow-hidden rounded-lg border border-neutral-300 bg-neutral-100 shadow-sm">
        <iframe
          src="/cv.pdf#view=FitH"
          title="Minghao Mou CV"
          className="block h-[min(78vh,1050px)] min-h-[720px] w-full"
        />
      </div>
    </main>
  );
}
