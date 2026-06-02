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

const RiskBadge = ({ level }) => {
  const styles = {
    High: 'text-red-500 font-semibold',
    Medium: 'text-amber-500 font-semibold',
    Low: 'text-green-500 font-semibold',
  };
  return <span className={styles[level] || 'text-gray-500'}>{level}</span>;
};

const statsData = [
  { icon: '👥', label: 'Assigned Youth', value: 42, link: 'View all', color: 'text-teal-600' },
  { icon: '⚠️', label: 'High-Risk Cases', value: 8, link: 'View alerts', color: 'text-amber-500' },
  { icon: '⏰', label: 'Aging Out in 6 Months', value: 11, link: 'View list', color: 'text-orange-500' },
  { icon: '📋', label: 'Follow-ups Due This Week', value: 18, link: 'View tasks', color: 'text-blue-600' },
];

const youthList = [
  { name: 'Amara Johnson', age: '17y 6m', risk: 'High', transition: 'May 15, 2026', followUp: '5/16/25', avatar: '👩🏾' },
  { name: 'Jalen Parker', age: '17y 2m', risk: 'Medium', transition: 'Aug 10, 2026', followUp: '5/19/25', avatar: '👦🏽' },
  { name: 'Maria Sanchez', age: '16y 11m', risk: 'Medium', transition: 'Jun 2, 2026', followUp: '5/20/25', avatar: '👧🏽' },
  { name: 'Tyler Williams', age: '17y 9m', risk: 'Low', transition: 'Oct 5, 2026', followUp: '5/21/25', avatar: '👦🏻' },
  { name: 'Lena Roberts', age: '17y 4m', risk: 'Medium', transition: 'Jul 18, 2026', followUp: '5/23/25', avatar: '👩🏼' },
];

const recentActivity = [
  { avatar: '👩🏾', name: 'Amara Johnson', action: 'Risk level updated to High', time: 'Today, 9:42 AM', color: 'text-red-500' },
  { avatar: '👧🏽', name: 'Maria Sanchez', action: 'Added education goal: CNA program', time: 'Today, 9:15 AM', color: 'text-teal-600' },
  { avatar: '👦🏽', name: 'Jalen Parker', action: 'Appointment completed', time: 'Yesterday, 3:20 PM', color: 'text-green-500' },
  { avatar: '👦🏻', name: 'Tyler Williams', action: 'Document uploaded: ID application', time: 'Yesterday, 1:05 PM', color: 'text-blue-600' },
  { avatar: '👩🏼', name: 'Lena Roberts', action: 'Housing plan updated', time: 'May 13, 2025', color: 'text-teal-600' },
];

const quickActions = [
  { icon: '➕', label: 'Add New Youth' },
  { icon: '📅', label: 'Schedule Appointment' },
  { icon: '✅', label: 'Create Follow-up Task' },
  { icon: '💬', label: 'Send Message' },
  { icon: '📄', label: 'Upload Document' },
  { icon: '📊', label: 'Run Risk Assessment' },
];

export default function CaseworkerDashboard({ onOpenAI }) {
  const [selectedYouth, setSelectedYouth] = useState(null);

  return (
    <div className="flex flex-col h-full bg-white rounded-2xl overflow-hidden shadow-lg" style={{ minHeight: 700 }}>
      {/* Header */}
      <div className="flex items-center justify-between px-5 py-3 border-b border-gray-100">
        <FuturePathLogo />
        <div className="flex items-center gap-3">
          <div className="text-right">
            <div className="text-xs font-semibold text-gray-800">Denise Carter</div>
            <div className="text-xs text-gray-500">Caseworker</div>
          </div>
          <button>
            <span className="text-gray-500 text-lg">🔔</span>
          </button>
        </div>
      </div>

      {/* Scrollable content */}
      <div className="flex-1 overflow-y-auto px-5 py-4 space-y-4">
        {/* Stats Row */}
        <div className="grid grid-cols-4 gap-3">
          {statsData.map((stat) => (
            <div key={stat.label} className="bg-white border border-gray-200 rounded-xl p-3 shadow-sm">
              <div className="flex items-center gap-1 mb-1">
                <span className="text-base">{stat.icon}</span>
                <span className="text-xs text-gray-500 leading-tight">{stat.label}</span>
              </div>
              <div className="text-2xl font-bold text-gray-800">{stat.value}</div>
              <button className={`text-xs mt-1 ${stat.color}`}>{stat.link}</button>
            </div>
          ))}
        </div>

        {/* High-Risk Alerts */}
        <div className="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
          <div className="flex items-center justify-between px-4 py-3 border-b border-gray-100">
            <div className="flex items-center gap-2">
              <span className="text-red-500">⚠️</span>
              <span className="text-sm font-bold text-gray-800">High-Risk Alerts</span>
            </div>
            <button className="text-teal-600 text-xs font-medium">View all alerts</button>
          </div>
          <div className="px-4 py-3">
            <div className="flex items-start gap-3 p-3 bg-red-50 border border-red-100 rounded-xl">
              <div className="w-10 h-10 rounded-full bg-amber-200 flex items-center justify-center text-xl shrink-0">
                👩🏾
              </div>
              <div className="flex-1 min-w-0">
                <div className="text-sm font-semibold text-gray-800">Amara Johnson</div>
                <div className="text-xs text-gray-500">17 years, 6 months</div>
                <div className="text-xs text-red-500 font-medium mt-0.5">Aging out in 6 months</div>
              </div>
              <div className="flex-1 min-w-0">
                <ul className="text-xs text-gray-700 space-y-0.5">
                  <li className="flex items-center gap-1"><span className="text-red-400">•</span> No stable housing plan after 18</li>
                  <li className="flex items-center gap-1"><span className="text-red-400">•</span> Needs ID replacement</li>
                  <li className="flex items-center gap-1"><span className="text-red-400">•</span> Needs continued counseling</li>
                </ul>
              </div>
              <button
                onClick={() => setSelectedYouth('Amara')}
                className="bg-white border border-gray-200 text-gray-700 text-xs px-3 py-1.5 rounded-lg shadow-sm whitespace-nowrap"
              >
                Open Case
              </button>
            </div>
          </div>
        </div>

        {/* Assigned Youth Table */}
        <div className="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
          <div className="px-4 py-3 border-b border-gray-100">
            <span className="text-sm font-bold text-gray-800">Assigned Youth</span>
          </div>
          <table className="w-full text-xs">
            <thead>
              <tr className="border-b border-gray-100 text-gray-500">
                <th className="px-4 py-2 text-left font-medium">Youth</th>
                <th className="px-3 py-2 text-left font-medium">Age</th>
                <th className="px-3 py-2 text-left font-medium">Risk Level</th>
                <th className="px-3 py-2 text-left font-medium">Transition Date</th>
                <th className="px-3 py-2 text-left font-medium">Next Follow-up</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-50">
              {youthList.map((y) => (
                <tr key={y.name} className="hover:bg-gray-50 transition-colors">
                  <td className="px-4 py-2.5">
                    <div className="flex items-center gap-2">
                      <span className="text-base">{y.avatar}</span>
                      <span className="font-medium text-gray-800">{y.name}</span>
                    </div>
                  </td>
                  <td className="px-3 py-2.5 text-gray-600">{y.age}</td>
                  <td className="px-3 py-2.5"><RiskBadge level={y.risk} /></td>
                  <td className="px-3 py-2.5 text-gray-600">{y.transition}</td>
                  <td className="px-3 py-2.5 text-gray-600">{y.followUp}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <div className="px-4 py-2.5 border-t border-gray-100">
            <button className="text-teal-600 text-xs font-medium">View all assigned youth</button>
          </div>
        </div>

        {/* Bottom two-column grid */}
        <div className="grid grid-cols-2 gap-4">
          {/* Recent Case Activity */}
          <div className="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
            <div className="px-4 py-3 border-b border-gray-100">
              <span className="text-sm font-bold text-gray-800">Recent Case Activity</span>
            </div>
            <div className="divide-y divide-gray-50">
              {recentActivity.map((item) => (
                <div key={item.name + item.time} className="flex items-start gap-2.5 px-4 py-2.5">
                  <div className={`w-7 h-7 rounded-full flex items-center justify-center text-base shrink-0 ${item.color === 'text-red-500' ? 'bg-red-50' : item.color === 'text-green-500' ? 'bg-green-50' : 'bg-blue-50'}`}>
                    {item.avatar}
                  </div>
                  <div>
                    <span className="text-xs font-medium text-gray-800">{item.name}</span>
                    <span className="text-xs text-gray-500"> · {item.action}</span>
                    <div className="text-xs text-gray-400 mt-0.5">{item.time}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Quick Actions */}
          <div className="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
            <div className="px-4 py-3 border-b border-gray-100">
              <span className="text-sm font-bold text-gray-800">Quick Actions</span>
            </div>
            <div className="divide-y divide-gray-50">
              {quickActions.map((action) => (
                <button
                  key={action.label}
                  className="w-full flex items-center gap-2.5 px-4 py-2.5 text-left hover:bg-gray-50 transition-colors"
                >
                  <span className="text-base">{action.icon}</span>
                  <span className="text-xs text-gray-700">{action.label}</span>
                </button>
              ))}
              <div className="px-4 py-2.5">
                <button className="text-teal-600 text-xs font-medium">View all tools</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
