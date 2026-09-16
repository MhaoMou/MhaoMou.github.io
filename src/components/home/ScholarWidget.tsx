'use client';

import { motion } from 'framer-motion';
import { ExternalLink } from 'lucide-react';

interface ScholarWidgetProps {
  href?: string;
  title?: string;
  description?: string;
}

export default function ScholarWidget({
  href,
  title = 'Google Scholar',
  description = 'Publication profile and citation record.',
}: ScholarWidgetProps) {
  if (!href) {
    return null;
  }

  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.55 }}
      className="rounded-lg border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-900 p-5"
    >
      <h2 className="text-xl font-serif font-bold text-primary mb-2">{title}</h2>
      <p className="text-sm text-neutral-600 dark:text-neutral-500 mb-4">{description}</p>
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
