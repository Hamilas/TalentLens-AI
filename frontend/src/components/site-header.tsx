import Link from "next/link";
import { ThemeToggle } from "@/components/theme-toggle";

export function SiteHeader() {
  return (
    <header className="sticky top-0 z-20 border-b border-white/10 bg-black/20 backdrop-blur-md">
      <div className="container mx-auto flex items-center justify-between px-4 py-3">
        <Link href="/" className="flex items-center gap-2">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            aria-hidden
          >
            <circle cx="11" cy="11" r="7" stroke="#3b82f6" strokeWidth="2" />
            <line
              x1="16.2"
              y1="16.2"
              x2="21"
              y2="21"
              stroke="#60a5fa"
              strokeWidth="2"
              strokeLinecap="round"
            />
          </svg>
          <span className="text-lg font-bold tracking-tight text-white">
            TalentLens<span className="text-[#3b82f6]">-AI</span>
          </span>
        </Link>
        <ThemeToggle />
      </div>
    </header>
  );
}
