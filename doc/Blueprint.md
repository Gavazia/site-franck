# Blueprint: Architecture Design

## 1. System Overview
The Franck Bietry Portfolio is a statically generated (SSG) frontend powered by Next.js, combined with a dynamic Admin Panel communicating via an API with an InsForge backend. 

## 2. Tech Stack Definition (The Golden Path)
*   **Framework**: Next.js 16 (App Router) + React 19 + TypeScript.
*   **Styling**: Tailwind CSS 3.4 + Hero UI (Native Glassmorphism capabilities).
*   **Iconography**: Phosphor Icons (for a distinct, academic, and premium aesthetic. No Lucide needed since Hero UI is agnostic).
*   **Animation**: Framer Motion (Optimized for minimal main-thread blocking).
*   **Backend & DB**: InsForge (PostgreSQL-based edge backend).
*   **AI Engine**: Google AI Studio (Gemini 3.0) integrated via Vercel AI SDK for the intelligent Admin Copilot.
*   **State Management**: Zustand (Only used for the Admin Panel session state; the public site will rely on Next.js Server Components and URL state).
*   **Deployment**: Vercel.

## 3. Data Flow & Rendering Strategy

### Public Site (Read-Only)
*   **Pattern**: React Server Components (RSC) + Static Site Generation (SSG) / ISR (Incremental Static Regeneration).
*   **Flow**: Users request a page -> Next.js serves the cached HTML -> On-demand Revalidation occurs when the Admin updates a post in InsForge.
*   **SEO Advantage**: The HTML arrives fully rendered to Google's crawlers. Zero CLS (Cumulative Layout Shift).

### Admin Panel (Read/Write)
*   **Pattern**: Client-Side Rendering (CSR) within a protected `/admin-franck` route group.
*   **Flow**: Franck logs in -> Zustand holds session -> Client securely mutating data directly to InsForge using the SDK.

## 4. Component Architecture (Atomic Design)

*   `app/` (Next.js Application Router)
    *   `(public)/` (SSG Routes)
        *   `page.tsx` (Home/Portfolio Timeline)
        *   `articles/`
        *   `publications/`
    *   `(admin)/` (Protected Routes)
        *   `admin-franck/`
*   `components/`
    *   `ui/` (Hero UI primitives: Buttons, Cards, Inputs).
    *   `glass/` (Custom Glassmorphism containers).
    *   `blocks/` (Complex assemblies: TimelineNode, PublicationRenderer).
*   `lib/`
    *   `insforge.ts` (Singleton SDK client).
    *   `utils.ts` (Tailwind merge utilities).

## 5. Security & Authorization
*   Row Level Security (RLS) enabled on all InsForge tables.
    *   `articles`, `publications`, `classes_and_conferences`, `institutions`, `profile`: Public read access (`true`). Insert/Update/Delete restricted to authenticated admin user (`auth.uid() = admin_id`).
