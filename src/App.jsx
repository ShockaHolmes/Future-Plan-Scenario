import { useState } from 'react'
import TeenDashboard from './components/TeenDashboard'
import CaseworkerDashboard from './components/CaseworkerDashboard'
import AIAssistant from './components/AIAssistant'
import './App.css'

const tabs = [
  { id: 'all', label: 'All Three' },
  { id: 'teen', label: '① Teen Dashboard' },
  { id: 'caseworker', label: '② Caseworker Dashboard' },
  { id: 'ai', label: '③ Future Path AI Assistant' },
]

function App() {
  const [activeTab, setActiveTab] = useState('all')
  const [aiOpen, setAiOpen] = useState(false)

  return (
    <div className="min-h-screen bg-slate-100 p-4 md:p-6">
      {/* Tab selector */}
      <div className="flex gap-2 mb-5 flex-wrap justify-center">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`px-4 py-2 rounded-full text-sm font-semibold transition-all shadow-sm ${
              activeTab === tab.id
                ? 'bg-teal-700 text-white shadow-md'
                : 'bg-white text-gray-600 hover:bg-gray-50 border border-gray-200'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* ALL THREE side by side */}
      {activeTab === 'all' && (
        <div className="flex gap-4 items-start justify-center flex-wrap xl:flex-nowrap">
          {/* Teen */}
          <div className="flex flex-col items-center w-full max-w-sm">
            <div className="flex items-center gap-2 mb-3">
              <div className="w-7 h-7 rounded-full bg-teal-700 text-white flex items-center justify-center font-bold text-sm">1</div>
              <h2 className="text-base font-bold text-gray-700">Teen Dashboard</h2>
            </div>
            <div className="w-full">
              <TeenDashboard onOpenAI={() => { setActiveTab('ai') }} />
            </div>
          </div>

          {/* Caseworker */}
          <div className="flex flex-col items-center w-full max-w-2xl">
            <div className="flex items-center gap-2 mb-3">
              <div className="w-7 h-7 rounded-full bg-teal-700 text-white flex items-center justify-center font-bold text-sm">2</div>
              <h2 className="text-base font-bold text-gray-700">Caseworker Dashboard</h2>
            </div>
            <div className="w-full">
              <CaseworkerDashboard onOpenAI={() => setActiveTab('ai')} />
            </div>
          </div>

          {/* AI Assistant */}
          <div className="flex flex-col items-center w-full max-w-sm">
            <div className="flex items-center gap-2 mb-3">
              <div className="w-7 h-7 rounded-full bg-teal-700 text-white flex items-center justify-center font-bold text-sm">3</div>
              <h2 className="text-base font-bold text-gray-700">Future Path AI Assistant</h2>
            </div>
            <div className="w-full">
              <AIAssistant onClose={() => setActiveTab('teen')} />
            </div>
          </div>
        </div>
      )}

      {/* Individual views */}
      {activeTab === 'teen' && (
        <div className="flex flex-col items-center">
          <div className="w-full max-w-sm">
            <TeenDashboard onOpenAI={() => setActiveTab('ai')} />
          </div>
        </div>
      )}

      {activeTab === 'caseworker' && (
        <div className="flex flex-col items-center">
          <div className="w-full max-w-3xl">
            <CaseworkerDashboard onOpenAI={() => setActiveTab('ai')} />
          </div>
        </div>
      )}

      {activeTab === 'ai' && (
        <div className="flex flex-col items-center">
          <div className="w-full max-w-sm">
            <AIAssistant onClose={() => setActiveTab('teen')} />
          </div>
        </div>
      )}
    </div>
  )
}

export default App

