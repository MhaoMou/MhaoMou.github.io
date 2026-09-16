'use client';

import { motion } from 'framer-motion';
import { BarChart3, ExternalLink } from 'lucide-react';

interface ScholarTrendPoint {
  year: string;
  citations: number;
}

interface ScholarWidgetProps {
  href?: string;
  title?: string;
  description?: string;
  totalCitations?: number;
  hIndex?: number;
  i10Index?: number;
  lastChecked?: string;
  trend?: ScholarTrendPoint[];
}

export default function ScholarWidget({
  href,
  title = 'Google Scholar',
  description = 'Publication profile and citation record.',
  totalCitations = 0,
  hIndex = 0,
  i10Index = 0,
  lastChecked,
  trend = [],
}: ScholarWidgetProps) {
  if (!href) {
    return null;
  }

  const maxCitations = Math.max(...trend.map((point) => point.citations), 1);
  const metrics = [
    { label: 'citations', value: totalCitations },
    { label: 'h-index', value: hIndex },
    { label: 'i10-index', value: i10Index },
  ];

  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.55 }}
      className="rounded-lg border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-900 p-5"
    >
      <div className="mb-4 flex items-start justify-between gap-4">
        <div>
          <h2 className="text-xl font-serif font-bold text-primary mb-2">{title}</h2>
          <p className="text-sm text-neutral-600 dark:text-neutral-500">{description}</p>
        </div>
        <BarChart3 className="mt-1 h-5 w-5 shrink-0 text-accent" aria-hidden="true" />
      </div>

      <p className="sr-only">
        {totalCitations} citations, h-index {hIndex}, i10-index {i10Index}
      </p>

      <dl className="grid grid-cols-3 gap-3 mb-5">
        {metrics.map((metric) => (
          <div
            key={metric.label}
            className="rounded-md border border-neutral-200 dark:border-neutral-800 bg-neutral-50 dark:bg-neutral-950 px-3 py-3"
          >
            <dt className="text-[11px] uppercase tracking-normal text-neutral-500 dark:text-neutral-500">
              {metric.label}
            </dt>
            <dd className="mt-1 text-2xl font-semibold text-neutral-900 dark:text-neutral-100">
              {metric.value}
            </dd>
          </div>
        ))}
      </dl>

      <div className="mb-5">
        <div className="mb-2 flex items-center justify-between gap-3">
          <h3 className="text-sm font-semibold text-neutral-800 dark:text-neutral-200">Citation trend</h3>
          {lastChecked && (
            <span className="text-xs text-neutral-500 dark:text-neutral-500">
              Last checked: {lastChecked}
            </span>
          )}
        </div>

        {trend.length > 0 ? (
          <div
            className="flex h-28 items-end gap-3 border-l border-b border-neutral-200 dark:border-neutral-800 px-2 pt-2"
            role="img"
            aria-label={`Citation trend: ${trend.map((point) => `${point.year}: ${point.citations}`).join(', ')}`}
          >
            {trend.map((point) => (
              <div key={point.year} className="flex h-full min-w-10 flex-1 flex-col items-center justify-end gap-2">
                <div className="text-xs font-medium text-neutral-700 dark:text-neutral-300">
                  {point.citations}
                </div>
                <div
                  className="w-full max-w-12 rounded-t-sm bg-accent"
                  style={{ height: `${Math.max((point.citations / maxCitations) * 72, 6)}px` }}
                  aria-hidden="true"
                />
                <div className="text-xs text-neutral-500 dark:text-neutral-500">{point.year}</div>
              </div>
            ))}
          </div>
        ) : (
          <p className="rounded-md border border-dashed border-neutral-200 dark:border-neutral-800 px-3 py-4 text-sm text-neutral-500 dark:text-neutral-500">
            Citation trend data is not available yet.
          </p>
        )}
      </div>

      <a
        href={href}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center gap-2 rounded-md bg-neutral-100 dark:bg-neutral-800 px-3 py-2 text-sm font-medium text-neutral-700 dark:text-neutral-300 transition-colors hover:bg-accent hover:text-white"
      >
        View profile
        <ExternalLink className="h-4 w-4" />
      </a>
    </motion.section>
  );
}
