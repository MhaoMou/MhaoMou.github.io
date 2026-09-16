'use client';

import Link from 'next/link';
import { motion } from 'framer-motion';
import { BlogPageConfig } from '@/types/page';

interface BlogPageProps {
  config: BlogPageConfig;
}

export default function BlogPage({ config }: BlogPageProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.4 }}
      className="max-w-3xl mx-auto"
    >
      <h1 className="text-4xl font-serif font-bold text-primary mb-4">{config.title}</h1>
      {config.description && (
        <p className="text-lg text-neutral-600 dark:text-neutral-500 mb-8 max-w-2xl">
          {config.description}
        </p>
      )}
      <div className="space-y-4">
        {config.posts.map((post) => (
          <Link
            key={post.slug}
            href={`/blog/${post.slug}`}
            className="block rounded-lg border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-900 p-5 transition-all duration-200 hover:border-accent hover:shadow-md"
          >
            <div className="text-xs text-neutral-500 mb-2">{post.date}</div>
            <h2 className="text-xl font-semibold text-primary mb-2">{post.title}</h2>
            <p className="text-sm text-neutral-600 dark:text-neutral-500 mb-3">{post.summary}</p>
            {post.tags && post.tags.length > 0 && (
              <div className="flex flex-wrap gap-2">
                {post.tags.map((tag) => (
                  <span
                    key={tag}
                    className="text-xs rounded-md bg-neutral-100 dark:bg-neutral-800 px-2 py-1 text-neutral-600 dark:text-neutral-400"
                  >
                    {tag}
                  </span>
                ))}
              </div>
            )}
          </Link>
        ))}
      </div>
    </motion.div>
  );
}
