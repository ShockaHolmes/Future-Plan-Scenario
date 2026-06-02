import { useState } from 'react';

const questions = [
  {
    id: 1,
    category: 'Housing',
    question: 'What is your plan for where you will live after you turn 18?',
    options: [
      { id: 'A', text: 'I have a stable place lined up' },
      { id: 'B', text: "I'm working on a plan" },
      { id: 'C', text: "I don't have a plan yet" },
      { id: 'D', text: "I'm not sure" },
    ],
    needCategory: 'Housing Stability',
    riskImpact: 'High',
    riskIcon: '🏠',
  },
  {
    id: 2,
    category: 'Education & Career',
    question: 'What are your plans for education or work after 18?',
    options: [
      { id: 'A', text: 'I have a job lined up' },
      { id: 'B', text: 'I plan to attend college or trade school' },
      { id: 'C', text: "I'm exploring options" },
      { id: 'D', text: "I don't have a plan yet" },
    ],
    needCategory: 'Education & Career',
    riskImpact: 'Medium',
    riskIcon: '🎓',
  },
  {
    id: 3,
    category: 'Health',
    question: 'Do you have access to health insurance after you turn 18?',
    options: [
      { id: 'A', text: 'Yes, through Medicaid or employer' },
      { id: 'B', text: "I'm applying for coverage" },
      { id: 'C', text: 'No, I need help finding coverage' },
      { id: 'D', text: "I'm not sure" },
    ],
    needCategory: 'Health & Wellness',
    riskImpact: 'Medium',
    riskIcon: '💚',
  },
];

const resources = [
  { icon: '🏠', title: 'Independent Living Services', desc: 'Support with housing, budgeting, and life skills.' },
  { icon: '🤝', title: 'Aftercare / ASSIST (18-21)', desc: 'Extended support for young adults.' },
  { icon: '📜', title: 'Delaware Tuition Waiver', desc: 'Financial support for eligible students.' },
  { icon: '💚', title: 'Mental Health Counseling', desc: 'Continued support for mental wellness.' },
  { icon: '🪪', title: 'ID / Document Readiness', desc: 'Help replacing ID and important documents.' },
];

export default function AIAssistant({ onClose }) {
  const [currentQ, setCurrentQ] = useState(0);
  const [answers, setAnswers] = useState({});
  const [showSummary, setShowSummary] = useState(false);
  const [chatMessage, setChatMessage] = useState('');

  const q = questions[currentQ];
  const total = questions.length + 7; // "10 total"
  const progress = Math.round(((currentQ + 1) / total) * 100);

  const handleAnswer = (optionId) => {
    setAnswers({ ...answers, [q.id]: optionId });
    if (currentQ < questions.length - 1) {
      setTimeout(() => setCurrentQ(currentQ + 1), 300);
    } else {
      setTimeout(() => setShowSummary(true), 300);
    }
  };

  const selectedOption = answers[q?.id];

  return (
    <div className="flex flex-col h-full bg-white rounded-2xl overflow-hidden shadow-lg" style={{ minHeight: 700 }}>
      {/* Header */}
      <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100">
        <div className="flex items-center gap-2">
          <div className="w-7 h-7 rounded-full bg-teal-600 flex items-center justify-center">
            <span className="text-white text-xs">🤖</span>
          </div>
          <span className="text-sm font-semibold text-gray-800">Future Path AI Assistant</span>
        </div>
        <div className="flex items-center gap-3">
          <button className="text-sm text-gray-500 hover:text-gray-700" onClick={onClose}>Close</button>
          <button className="text-gray-400 hover:text-gray-600 text-lg leading-none" onClick={onClose}>✕</button>
        </div>
      </div>

      {/* Scrollable content */}
      <div className="flex-1 overflow-y-auto px-4 py-4 space-y-4">
        {!showSummary ? (
          <>
            {/* Progress */}
            <div>
              <div className="flex justify-between text-xs text-gray-500 mb-1">
                <span>Question {currentQ + 1} of {total}</span>
                <span>{progress}%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div
                  className="bg-teal-600 h-2 rounded-full transition-all duration-500"
                  style={{ width: `${progress}%` }}
                />
              </div>
            </div>

            {/* Question Card */}
            <div className="bg-blue-50 border border-blue-100 rounded-xl p-4">
              <div className="text-xs font-semibold text-teal-700 mb-2">Let's start with {q.category.toLowerCase()}.</div>
              <div className="text-sm font-semibold text-gray-800 leading-snug">{q.question}</div>
            </div>

            {/* Options */}
            <div className="space-y-2">
              {q.options.map((opt) => {
                const isSelected = selectedOption === opt.id;
                return (
                  <button
                    key={opt.id}
                    onClick={() => handleAnswer(opt.id)}
                    className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl border text-left transition-all ${
                      isSelected
                        ? 'bg-teal-700 border-teal-700 text-white'
                        : 'bg-white border-gray-200 text-gray-700 hover:border-teal-400 hover:bg-teal-50'
                    }`}
                  >
                    <span className={`w-6 h-6 rounded-full border flex items-center justify-center text-xs font-bold shrink-0 ${
                      isSelected ? 'border-teal-300 text-teal-200' : 'border-gray-300 text-gray-500'
                    }`}>
                      {opt.id}
                    </span>
                    <span className="text-sm">{opt.text}</span>
                    {isSelected && <span className="ml-auto">✓</span>}
                  </button>
                );
              })}
            </div>

            {/* Need Category Triggered */}
            <div className="grid grid-cols-2 gap-3">
              <div className="bg-white border border-gray-200 rounded-xl p-3">
                <div className="text-xs text-gray-500 mb-2">Need Category Triggered</div>
                <div className="flex items-center gap-2 bg-teal-50 text-teal-700 text-xs font-medium px-3 py-1.5 rounded-lg w-fit">
                  <span>{q.riskIcon}</span>
                  <span>{q.needCategory}</span>
                </div>
              </div>
              <div className="bg-white border border-gray-200 rounded-xl p-3">
                <div className="text-xs text-gray-500 mb-2">Risk Impact</div>
                <div className={`flex items-center gap-1 text-xs font-semibold px-3 py-1.5 rounded-lg w-fit ${
                  q.riskImpact === 'High' ? 'bg-red-50 text-red-600' : 'bg-amber-50 text-amber-600'
                }`}>
                  <span>⚠️</span>
                  <span>{q.riskImpact}</span>
                </div>
              </div>
            </div>
          </>
        ) : (
          /* Assessment Summary */
          <div className="space-y-4">
            <h3 className="text-sm font-bold text-gray-800">Your Assessment Summary</h3>
            <div className="grid grid-cols-2 gap-3">
              <div className="bg-white border border-gray-200 rounded-xl p-3">
                <div className="text-xs text-gray-500 mb-2">Overall Risk Level</div>
                <div className="flex items-center gap-1 text-red-600 font-bold text-sm">
                  <span>⚠️</span>
                  <span>High</span>
                </div>
              </div>
              <div className="bg-white border border-gray-200 rounded-xl p-3">
                <div className="text-xs text-gray-500 mb-2">Top Need</div>
                <div className="flex items-center gap-1 text-teal-600 font-semibold text-sm">
                  <span>🏠</span>
                  <span>Housing Stability</span>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Recommended Resources - always visible after first question answered */}
        {(showSummary || Object.keys(answers).length > 0) && (
          <div>
            <h3 className="text-sm font-bold text-gray-800 mb-3">Recommended Resources</h3>
            <div className="space-y-2">
              {resources.map((r) => (
                <div key={r.title} className="flex items-start gap-3 p-3 bg-white border border-gray-200 rounded-xl">
                  <div className="w-9 h-9 bg-teal-50 rounded-lg flex items-center justify-center text-base shrink-0">
                    {r.icon}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="text-xs font-semibold text-gray-800">{r.title}</div>
                    <div className="text-xs text-gray-500 mt-0.5">{r.desc}</div>
                  </div>
                  <button className="text-teal-600 text-xs font-medium whitespace-nowrap">View</button>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Bottom chat prompt */}
      <div className="border-t border-gray-100 bg-gray-50 px-4 py-3 space-y-2">
        <div className="flex items-start gap-2">
          <div className="w-8 h-8 bg-teal-600 rounded-full flex items-center justify-center shrink-0">
            <span className="text-white text-xs">🤖</span>
          </div>
          <div className="flex-1 bg-white border border-gray-200 rounded-xl px-3 py-2">
            <p className="text-xs text-gray-600">I'm here to help. What would you like to do next?</p>
          </div>
          <button className="bg-white border border-gray-200 text-xs text-gray-700 px-3 py-1.5 rounded-lg whitespace-nowrap">
            Ask a question
          </button>
          <button className="bg-white border border-gray-200 text-xs text-gray-700 px-3 py-1.5 rounded-lg whitespace-nowrap">
            Explore resources
          </button>
        </div>
        <div className="flex items-center gap-2">
          <input
            value={chatMessage}
            onChange={(e) => setChatMessage(e.target.value)}
            onFocus={() => {}}
            placeholder="Type your message..."
            className="flex-1 bg-white border border-gray-200 rounded-full px-4 py-2 text-xs outline-none focus:border-teal-400"
          />
          <button
            className={`w-8 h-8 rounded-full flex items-center justify-center transition-colors ${
              chatMessage.trim() ? 'bg-teal-600' : 'bg-gray-200'
            }`}
          >
            <svg viewBox="0 0 24 24" className={`w-4 h-4 ${chatMessage.trim() ? 'text-white' : 'text-gray-400'} fill-current`}>
              <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
}
