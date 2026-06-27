"use client";

import { AnalysisDashboard } from "@/components/analysis-dashboard";
import { SiteHeader } from "@/components/site-header";
import { LoadingSpinner } from "@/components/ui/loading-spinner";
import type { TranscriptSummary } from "@/types/interview";
import { useRouter, useSearchParams } from "next/navigation";
import { Suspense, useEffect, useState } from "react";

export default function AnalysisPage() {
  return (
    <Suspense
      fallback={
        <div className="px-4 py-12 text-center text-white/70">
          <LoadingSpinner size="md" className="mx-auto" />
        </div>
      }
    >
      <AnalysisPageContent />
    </Suspense>
  );
}

function AnalysisPageContent() {
  const params = useSearchParams();
  const router = useRouter();
  const [summary, setSummary] = useState<TranscriptSummary | null>(null);

  useEffect(() => {
    const cached = sessionStorage.getItem("analysis:summary");
    if (cached) setSummary(JSON.parse(cached) as TranscriptSummary);
  }, [params]);

  return (
    <main className="relative min-h-screen overflow-hidden bg-slate-50 dark:bg-black">
      <SiteHeader />
      <div className="container mx-auto px-4 py-6">
        {/* Top header with back + action */}
        <div className="mb-6 flex items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <button
              onClick={() => {
                try {
                  sessionStorage.removeItem("analysis:summary");
                } catch {}
                router.push("/");
              }}
              className="cursor-pointer rounded-full border border-white/15 px-3 py-1.5 text-sm text-white/80 hover:bg-white/5"
            >
              <span className="sm:hidden" aria-hidden>
                ←
              </span>
              <span className="hidden items-center gap-2 sm:inline-flex">
                ← <span>Back</span>
              </span>
            </button>
            <h1 className="truncate text-base font-semibold text-white/90 sm:text-lg">
              Interview Insights
            </h1>
          </div>
          {summary && (
            <button
              onClick={() => {
                try {
                  sessionStorage.removeItem("analysis:summary");
                } catch {}
                router.push("/");
              }}
              className="cursor-pointer rounded-full bg-[#00A3E0] px-3 py-1.5 text-xs text-white font-semibold hover:bg-[#14b5f1] sm:text-sm"
            >
              New Analysis
            </button>
          )}
        </div>

        {!summary ? (
          <div className="px-4 py-12 text-center text-white/70">
            <LoadingSpinner size="md" className="mx-auto" />
            <p className="mt-3 text-sm">Preparing your analysis...</p>
          </div>
        ) : (
          <div className="py-2">
            <AnalysisDashboard summary={summary} />
          </div>
        )}
      </div>
    </main>
  );
}
