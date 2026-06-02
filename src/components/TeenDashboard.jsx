import { useState } from 'react';

const FuturePathLogo = () => (
  <div className="flex items-center gap-1.5">
    <div className="w-7 h-7 rounded-full bg-teal-600 flex items-center justify-center">
      <svg viewBox="0 0 24 24" className="w-4 h-4 text-white fill-current">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
      </svg>
    </div>
    <span className="font-semibold text-gray-800 text-sm">Future Path</span>
  </div>
);

const ProgressBar = ({ value, color = 'bg-teal-600' }) => (
  <div className="w-full bg-gray-200 rounded-full h-1.5 mt-1">
    <div className={`${color} h-1.5 rounded-full`} style={{ width: `${value}%` }} />
  </div>
);

const priorities = [
  {
    icon: '🏠',
    iconBg: 'bg-teal-50',
    title: 'Housing Plan',
    desc: 'Build a stable plan for when you turn 18.',
    progress: 60,
  },
  {
    icon: '🪪',
    iconBg: 'bg-teal-50',
    title: 'State ID Replacement',
    desc: 'Replace your State ID before it expires.',
    progress: 40,
  },
  {
    icon: '🎓',
    iconBg: 'bg-teal-50',
    title: 'CNA / Delaware Tech Pathway',
    desc: 'Complete CNA training & explore Delaware Tech.',
    progress: 75,
  },
  {
    icon: '❤️',
    iconBg: 'bg-teal-50',
    title: 'Counseling Support',
    desc: 'Continue counseling for anxiety and trauma.',
    progress: 50,
  },
];

const lifeAreas = [
  { label: 'Housing Stability', value: 60 },
  { label: 'Education & Career', value: 70 },
  { label: 'Health & Wellness', value: 55 },
  { label: 'Documents & ID', value: 40 },
  { label: 'Life Skills & Finances', value: 35 },
];

const supports = [
  { icon: '🏠', label: 'Independent Living Services' },
  { icon: '🤝', label: 'Aftercare / ASSIST (18-21)' },
  { icon: '📜', label: 'Delaware Tuition Waiver' },
  { icon: '🪪', label: 'ID / Document Readiness' },
  { icon: '💚', label: 'Mental Health Counseling' },
];

const navItems = [
  { icon: '🏠', label: 'Home', active: true },
  { icon: '📋', label: 'Plan' },
  { icon: '📅', label: 'Appointments' },
  { icon: '🔗', label: 'Resources' },
  { icon: '💬', label: 'Messages' },
];

export default function TeenDashboard({ onOpenAI }) {
  const [activeNav, setActiveNav] = useState('Home');

  return (
    <div className="flex flex-col h-full bg-white rounded-2xl overflow-hidden shadow-lg" style={{ minHeight: 700 }}>
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100">
        <FuturePathLogo />
        <div className="flex items-center gap-3">
          <button className="relative">
            <span className="text-gray-500 text-lg">🔔</span>
          </button>
          <div className="w-8 h-8 rounded-full bg-amber-600 overflow-hidden flex items-center justify-center">
            <span className="text-white text-xs font-bold">A</span>
          </div>
        </div>
      </div>

      {/* Scrollable content */}
      <div className="flex-1 overflow-y-auto">
        {/* Hero welcome */}
        <div className="relative bg-gradient-to-br from-teal-700 to-teal-500 px-4 pt-4 pb-6 overflow-hidden">
          <div className="absolute right-0 bottom-0 w-32 opacity-20">
            <div className="w-32 h-32 bg-teal-300 rounded-full translate-x-8 translate-y-4" />
          </div>
          <div className="relative z-10 flex justify-between items-start">
            <div>
              <h2 className="text-white text-xl font-bold mb-1">Hi Amara! 👋</h2>
              <p className="text-teal-100 text-sm leading-snug">
                We're here to help you build your<br />best future.
              </p>
            </div>
            <div className="w-20 h-20 rounded-full bg-teal-400 overflow-hidden border-2 border-white shadow-md flex items-center justify-center">
              <span className="text-3xl">👩🏾</span>
            </div>
          </div>
        </div>

        {/* Transition Plan Card */}
        <div className="mx-4 -mt-3 bg-white rounded-xl shadow-md p-4 border border-gray-100">
          <div className="flex justify-between items-start mb-2">
            <span className="text-sm font-semibold text-gray-800">Your Transition Plan</span>
            <div className="text-right">
              <div className="text-xs text-gray-500">Transition Date</div>
              <div className="text-teal-600 font-bold text-sm">180 days</div>
              <div className="text-xs text-gray-500">May 15, 2026</div>
            </div>
          </div>
          <ProgressBar value={68} />
          <div className="flex justify-between mt-1">
            <span className="text-xs text-gray-500">Keep going! You're making great progress.</span>
            <span className="text-xs font-semibold text-teal-600">68% complete</span>
          </div>
        </div>

        {/* Top Priorities */}
        <div className="px-4 mt-4">
          <h3 className="text-sm font-bold text-gray-800 mb-3">Top Priorities</h3>
          <div className="grid grid-cols-2 gap-2">
            {priorities.map((p) => (
              <div key={p.title} className="bg-white rounded-xl border border-gray-100 shadow-sm p-3">
                <div className={`w-8 h-8 ${p.iconBg} rounded-lg flex items-center justify-center mb-2`}>
                  <span className="text-base">{p.icon}</span>
                </div>
                <div className="text-xs font-semibold text-gray-800 leading-tight mb-1">{p.title}</div>
                <div className="text-xs text-gray-500 leading-tight mb-2">{p.desc}</div>
                <ProgressBar value={p.progress} />
                <div className="text-right mt-0.5">
                  <span className="text-xs text-gray-500">{p.progress}%</span>
                </div>
                <div className="text-right mt-1">
                  <span className="text-gray-400 text-sm">›</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Life Area Progress */}
        <div className="px-4 mt-4">
          <h3 className="text-sm font-bold text-gray-800 mb-3">Life Area Progress</h3>
          <div className="bg-white rounded-xl border border-gray-100 shadow-sm p-4 space-y-3">
            {lifeAreas.map((area) => (
              <div key={area.label} className="flex items-center gap-2">
                <span className="text-xs text-gray-600 w-28 shrink-0">{area.label}</span>
                <div className="flex-1">
                  <ProgressBar value={area.value} color="bg-teal-500" />
                </div>
                <span className="text-xs text-gray-500 w-8 text-right">{area.value}%</span>
              </div>
            ))}
          </div>
        </div>

        {/* Upcoming Appointment */}
        <div className="px-4 mt-4">
          <div className="bg-white rounded-xl border border-gray-100 shadow-sm p-4">
            <h3 className="text-sm font-bold text-gray-800 mb-2">Upcoming Appointment</h3>
            <div className="flex gap-3 items-start">
              <div className="w-9 h-9 bg-blue-50 rounded-lg flex items-center justify-center shrink-0">
                <span className="text-base">📅</span>
              </div>
              <div>
                <div className="text-xs font-semibold text-gray-700">Fri, May 16, 2025 · 10:00 AM</div>
                <div className="text-xs text-gray-800 font-medium mt-0.5">Counseling Session</div>
                <div className="text-xs text-gray-500 mt-0.5">Dover Counseling Center</div>
                <div className="text-xs text-gray-500">123 Walker Rd, Dover, DE 19904</div>
                <button className="mt-2 bg-teal-600 text-white text-xs px-4 py-1.5 rounded-full font-medium">
                  View Details
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Recommended Supports */}
        <div className="px-4 mt-4">
          <h3 className="text-sm font-bold text-gray-800 mb-2">Recommended Supports</h3>
          <div className="bg-white rounded-xl border border-gray-100 shadow-sm divide-y divide-gray-50">
            {supports.map((s) => (
              <div key={s.label} className="flex items-center justify-between px-3 py-2.5">
                <div className="flex items-center gap-2">
                  <span className="text-base">{s.icon}</span>
                  <span className="text-xs text-gray-700">{s.label}</span>
                </div>
                <span className="text-gray-400 text-sm">›</span>
              </div>
            ))}
          </div>
          <div className="text-center mt-2">
            <button className="text-teal-600 text-xs font-medium">See all supports</button>
          </div>
        </div>

        {/* Chat with Future Path AI */}
        <div className="px-4 mt-4 mb-4">
          <div className="bg-teal-50 rounded-xl border border-teal-100 p-4 flex items-start gap-3">
            <div className="w-9 h-9 bg-teal-600 rounded-full flex items-center justify-center shrink-0">
              <span className="text-white text-base">🤖</span>
            </div>
            <div className="flex-1">
              <div className="text-sm font-semibold text-gray-800">Chat with Future Path AI</div>
              <div className="text-xs text-gray-500 mt-0.5">Ask questions, get guidance, and find the right resources.</div>
            </div>
          </div>
          <div className="text-center mt-2">
            <button
              onClick={onOpenAI}
              className="bg-teal-700 text-white text-sm px-6 py-2 rounded-full font-medium shadow"
            >
              Start Chat
            </button>
          </div>
        </div>
      </div>

      {/* Bottom Nav */}
      <div className="border-t border-gray-200 bg-white">
        <div className="flex">
          {navItems.map((item) => (
            <button
              key={item.label}
              onClick={() => setActiveNav(item.label)}
              className={`flex-1 flex flex-col items-center py-2 gap-0.5 ${
                activeNav === item.label ? 'text-teal-600' : 'text-gray-400'
              }`}
            >
              <span className="text-lg">{item.icon}</span>
              <span className="text-xs">{item.label}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
