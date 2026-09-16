import { notFound } from 'next/navigation';
import { Metadata } from 'next';
import { getPageConfig, getBlogMarkdownContent } from '@/lib/content';
import BlogPostPage from '@/components/pages/BlogPostPage';
import { BlogPageConfig } from '@/types/page';

function getBlogConfig(): BlogPageConfig | null {
  return getPageConfig<BlogPageConfig>('blog');
}

export function generateStaticParams() {
  const config = getBlogConfig();
  return (config?.posts || []).map((post) => ({ post: post.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ post: string }> }): Promise<Metadata> {
  const { post: slug } = await params;
  const config = getBlogConfig();
  const post = config?.posts.find((item) => item.slug === slug);

  if (!post) {
    return {};
  }

  return {
    title: `${post.title} | Blog`,
    description: post.summary,
  };
}

export default async function BlogPostRoute({ params }: { params: Promise<{ post: string }> }) {
  const { post: slug } = await params;
  const config = getBlogConfig();
  const post = config?.posts.find((item) => item.slug === slug);

  if (!post) {
    notFound();
  }

  const content = getBlogMarkdownContent(post.source);

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <BlogPostPage post={post} content={content} />
    </div>
  );
}
