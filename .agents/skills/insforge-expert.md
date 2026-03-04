---
name: InsForge Integration Protocol
description: Standard Operating Procedure (SOP) for setting up and using InsForge in Next.js 16 projects, including database operations and AI capabilities.
---

# InsForge Integration Guide

This skill document defines the Golden Path for integrating InsForge into our SaaS Factory V3 architecture. As the backend replacement for Supabase, InsForge provides built-in AI capabilities and Database management.

## 1. Installation & Setup

InsForge provides a dedicated SDK for TypeScript/Next.js.

### Dependencies
```bash
npm install @insforge/sdk
```

### Environment Variables
Required in `.env.local`:
```env
NEXT_PUBLIC_INSFORGE_URL=https://your-project.us-east.insforge.app
NEXT_PUBLIC_INSFORGE_ANON_KEY=your-anon-key
```

### Client Initialization (lib/insforge.ts)
Create a single instance of the client to be used across the application.

```typescript
import { createClient } from '@insforge/sdk';

// Golden Path Standard: Always export a singleton instance
export const insforge = createClient({
  baseUrl: process.env.NEXT_PUBLIC_INSFORGE_URL!,
  anonKey: process.env.NEXT_PUBLIC_INSFORGE_ANON_KEY!,
});
```

## 2. Database Operations (CRUD)

InsForge syntax is heavily inspired by standard BaaS providers. Use it seamlessly in Next.js Server Components.

### Fetching Data (Server Component Example)
```typescript
import { insforge } from '@/lib/insforge';

export default async function DataPage() {
  // Pattern: Destructure data and error
  const { data: records, error } = await insforge.database
    .from('your_table_name')
    .select();

  if (error) {
    console.error("InsForge Fetch Error:", error.message);
    return <div>Failed to load data.</div>;
  }

  return (
    <div>
      {records?.map((record) => (
        <div key={record.id}>{record.name}</div>
      ))}
    </div>
  );
}
```

## 3. Storage Operations

InsForge handles file uploads (Images, PDFs) which is critical for the Franck Portfolio project.

*(Note: Specific Storage syntax should follow standard BaaS patterns `insforge.storage.from('bucket').upload()`. Assumed based on architecture parity until specific docs are crawled).*

## 4. AI Capabilities

InsForge's primary differentiator is its built-in AI layer.
- Ensure to utilize the AI layer for search, chat completions, or data processing as required by the PRD.

## 5. Security Checklist
- [ ] Never expose `SERVICE_ROLE` or admin keys in the frontend.
- [ ] Always use the `NEXT_PUBLIC` prefix ONLY for the Anon Key.
- [ ] Validate all inputs using `zod` before sending mutations to InsForge.
