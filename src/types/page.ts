export interface BasePageConfig {
    type: 'about' | 'publication' | 'card' | 'text' | 'blog';
    title: string;
    description?: string;
}

export interface PublicationPageConfig extends BasePageConfig {
    type: 'publication';
    source: string;
}

export interface TextPageConfig extends BasePageConfig {
    type: 'text';
    source: string;
}

export interface CardItem {
    title: string;
    subtitle?: string;
    date?: string;
    content?: string;
    tags?: string[];
    link?: string;
    image?: string;
}

export interface CardPageConfig extends BasePageConfig {
    type: 'card';
    items: CardItem[];
}

export interface BlogPostMeta {
    slug: string;
    title: string;
    date: string;
    summary: string;
    tags?: string[];
    source: string;
}

export interface BlogPageConfig extends BasePageConfig {
    type: 'blog';
    posts: BlogPostMeta[];
}
