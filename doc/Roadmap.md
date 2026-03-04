# Execution Roadmap: Franck Bietry Portfolio

## Overview
This roadmap is designed to move from concept to a production-ready Vercel deployment with zero technical debt, using Next.js 16 and InsForge.

## Sprint 1: Foundation & Data Migration (Week 1)
**Goal:** Establish the technical skeleton and transition legacy Google Sites content into the new database.
*   **Step 1.1**: Initialize Next.js 16 `app` router project with Tailwind, TypeScript, and Shadcn/ui.
*   **Step 1.2**: Configure `insforge.ts` SDK connection and setup `.env` variables.
*   **Step 1.3**: In InsForge, create the 5 core tables (`profile`, `articles`, `publications`, `classes_and_conferences`, `institutions`) and configure Storage buckets for assets.
*   **Step 1.4**: Run the Firecrawl data extraction script. Parse the returned markdown and push initial data seeds into the InsForge database. Upload scraped images/PDFs to Storage.

## Sprint 2: The Glassmorphism Frontend (Week 2)
**Goal:** Build the public-facing read-only application with the desired "Innovative Glass" aesthetic.
*   **Step 2.1**: Set up global CSS tokens for the glass effect (backdrop filters, custom drop shadows, typography).
*   **Step 2.2**: Build the `app/page.tsx` (Profile + Vertical Institution Carousel).
*   **Step 2.3**: Build the chronological Timeline component for `app/journey` (Classes & Conferences) utilizing Framer Motion for scroll reveals.
*   **Step 2.4**: Build the Academic Publications archive (`app/publications`) with filtering capabilities.
*   **Step 2.5**: Build the Blog layout (`app/blog`).

## Sprint 3: The Admin Panel & SEO Lock (Week 3)
**Goal:** Secure the CMS for Franck and ensure 100% SEO compliance.
*   **Step 3.1**: Implement InsForge Auth for the `/admin-franck` route group.
*   **Step 3.2**: Build the minimal admin dashboard (CRUD operations for the 5 core tables).
*   **Step 3.3**: Integrate a rich text block editor for formatting blog posts within the admin panel.
*   **Step 3.4**: Implement dynamic `metadata` exports in all public Next.js routes. Structure JSON-LD (`Person`, `ScholarlyArticle`) specifically for "Franck Bietry".
*   **Step 3.5**: Final visual polish, Lighthouse auditing, and production deployment on Vercel. Map the legacy Google Sites URLs to new routes `seo_migration.json` via Next.js `next.config.js` redirects.
