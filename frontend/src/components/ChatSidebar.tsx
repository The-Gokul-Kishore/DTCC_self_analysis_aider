'use client';

import { ChatMessage } from '@/lib/types';
import { Bars3Icon, PlusIcon } from '@heroicons/react/24/outline';
import MotionWrapper from './MotionWrapper';

interface ChatSidebarProps {
  messages: ChatMessage[];
  onNewChat: () => void;
  onToggleSidebar: () => void;
}

export default function ChatSidebar({ messages, onNewChat, onToggleSidebar }: ChatSidebarProps) {
  // Group messages by date
  const groupedMessages = messages.reduce((groups, message) => {
    const date = message.timestamp.toLocaleDateString();
    if (!groups[date]) {
      groups[date] = [];
    }
    groups[date].push(message);
    return groups;
  }, {} as Record<string, ChatMessage[]>);

  return (
    <div className="h-full flex flex-col">
      {/* Header */}
      <div className="p-4 border-b border-purple-500/20 flex items-center justify-between">
        <h2 className="text-xl font-semibold text-white">Chat History</h2>
        <div className="flex space-x-2">
          <button
            onClick={onNewChat}
            className="p-2 text-gray-400 hover:text-white transition-colors"
          >
            <PlusIcon className="h-5 w-5" />
          </button>
          <button
            onClick={onToggleSidebar}
            className="p-2 text-gray-400 hover:text-white transition-colors"
          >
            <Bars3Icon className="h-5 w-5" />
          </button>
        </div>
      </div>

      {/* Chat History */}
      <div className="flex-1 overflow-y-auto p-4 space-y-6">
        {Object.entries(groupedMessages).map(([date, messages]) => (
          <div key={date} className="space-y-2">
            <h3 className="text-sm font-medium text-gray-400">{date}</h3>
            {messages.map((message) => (
              <MotionWrapper
                key={message.id}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                className="p-3 rounded-lg bg-gray-700/50 hover:bg-gray-700/70 cursor-pointer transition-colors"
              >
                <p className="text-sm text-gray-300 truncate">
                  {message.content}
                </p>
                <span className="text-xs text-gray-500">
                  {message.timestamp.toLocaleTimeString()}
                </span>
              </MotionWrapper>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
} 