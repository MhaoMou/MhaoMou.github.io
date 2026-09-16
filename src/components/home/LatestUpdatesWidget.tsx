'use client';

import { motion } from 'framer-motion';
import { NewsItem } from '@/components/home/News';

interface LatestUpdatesWidgetProps {
  items: NewsItem[];
  title?: string;
}

export default function LatestUpdatesWidget({ items, title = 'Latest Updates' }: LatestUpdatesWidgetProps) {
  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.5 }}
      className="rounded-lg border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-900 p-5"
    >
      <h2 className="text-xl font-serif font-bold text-primary mb-4">{title}</h2>
      <div className="space-y-3">
        {items.map((item, index) => (
          <div key={`${item.date}-${index}`} className="flex items-start gap-3">
            <span className="text-xs text-neutral-500 mt-1 w-16 flex-shrink-0">{item.date}</span>
            <p className="text-sm text-neutral-700 dark:text-neutral-500">{item.content}</p>
          </div>
        ))}
      </div>
    </motion.section>
  );
}
