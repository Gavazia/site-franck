# Product Requirements Document (PRD): Franck's Portfolio & Blog

## 1. Goal Description
The objective is to build a premium, highly optimized personal brand website and portfolio for Franck Bietry, a university professor. The site aims to consolidate his professional trajectory, academic publications, classes, and a standard blog into a unified, visually striking interface. The legacy Google Sites content will be migrated into a modern Next.js architecture powered by Inforg for content management and AI integrations.

## 2. User Review Required
> [!IMPORTANT]
> **Inforg Backend Configuration**: I need the specific connection details, SDK configuration steps, and any existing API keys for Inforg. Since it will serve as our CMS and backend, the project cannot proceed to the implementation database phase without this infrastructure setup.
> 
> **Content Categorization**: Please confirm the proposed data schemas (Section 3.1) precisely match the fields Franck needs for his publications and classes.

## 3. Architecture & Tech Stack

### 3.1 Data Schema (Inforg)
The backend will manage the following core entities:

*   **`articles`** (Well-structured Blog)
    *   `id`, `title`, `slug`, `content` (Rich Text/Markdown), `published_at`, `status`.
*   **`publications`** (Academic Papers - Structured & Filterable)
    *   `id`, `title`, `year`, `category`, `abstract`, `external_url`, `call_to_action` (Optional direct PDF link button). *No raw PDFs dumped here.*
*   **`classes_and_conferences`** (Chronological Journey)
    *   `id`, `title`, `date`, `institution_id` (foreign key), `description`, `visual_assets`.
*   **`institutions`** (Organizations)
    *   `id`, `name`, `logo_url`. Used for the horizontal scrolling logo carousel at the end of the profile section.
*   **`profile`** (The Core Identity)
    *   `id`, `full_name`, `bio_short`, `bio_long`, `current_roles`, `avatar_url`. This is the first thing users see.

### 3.2 Tech Stack Selection (Final & Locked)
*   **Framework**: Next.js 16 (App Router) + React 19 + TypeScript.
*   **Styling & UI**: Tailwind CSS 3.4 + Hero UI (for native blurred glass aesthetics).
*   **Iconography**: Phosphor Icons (Lucide-React replaced entirely as requested, since Hero UI allows agnostic iconography).
*   **Animations**: Framer Motion (for smooth scrolling and glassmorphism reveals).
*   **Backend & DB**: InsForge (PostgreSQL-based platform with Free Tier for Auth, DB, and Storage).
*   **AI Engine**: Google AI Studio (Gemini 3.0) integrated via Vercel AI SDK v5 for the intelligent Admin Copilot.
*   **Editor**: Novel.sh / TipTap (Minimalist, Notion-style block editor for the admin panel).
*   **Validation & State**: Zod (Typing) + Zustand (Admin session state).
*   **Deployment**: Vercel.

## 4. Proposed Changes & Features

### 4.1 Frontend / UI/UX Experience
*   **Aesthetic**: "Innovative Glassmorphism". Deep mode backgrounds (ice/crystal effect) with frosted glass cards. Text remains highly legible (crisp black/dark text on diffused light backgrounds) with glowing 3D-like drop shadows around the glass containers.
*   **Performance vs Visuals**: Highly visual experience with scroll-triggered transistions for the portfolio/journey, balanced with SEO optimization for articles and papers.
*   **SEO Target (CRITICAL)**: "Franck Bietry" must rank 100% #1 on Google. Static generation (SSG) for all public pages, optimized JSON-LD schemas (`Person`, `ScholarlyArticle`), and perfectly curated `<title>` and `<meta>` tags.
*   **Home/About Phase**: Immediate impact presenting *who he is*. Seamless horizontal carousel displaying logos of associated institutions at the bottom.

### 4.2 Content Pages
*   **Publications**: A structured archive, filterable by year or topic. Clean typography. No embedded PDFs; instead, a clear Call-to-Action (CTA) button to download the PDF or visit the external source.
*   **Classes/Conferences**: A visual, chronological timeline of his academic journey.
*   **Blog**: Standard rich-text articles, highly readable.

### 4.3 Backend Management (CMS)
*   **Admin Access**: Secure login to manage Inforg records.
*   **Content Editor**: Novel.sh / TipTap integrated into the admin route. A minimal, Notion-like block editor that saves structured data to InsForge.
*   **AI Copilot**: Integrated Vercel AI SDK powered by Gemini 3.0 via Google AI Studio. Franck can prompt the AI to correct grammar, optimize SEO, and re-format his text directly within the editor interface.

## 5. Verification Plan
### Automated Tests
*   `npm run build`: Ensure Next.js statically generates all dynamic routes successfully.
*   Lighthouse CLI: Run performance and SEO audits targeting 95+ scores specifically for the `/publications` and `/` routes.

### Manual Verification
*   **Scraping Audit**: Review the generated Markdown files from Firecrawl in `Asset/Scraped_Content/` to ensure no data loss.
*   **UI QA**: Verify the "glassmorphism" effect across Chrome, Safari, and mobile viewports. Check Framer Motion scroll animations for dropped frames.
*   **SEO Check**: Inspect rendered DOM to confirm JSON-LD injection and correct meta tag population for Franck's name.
