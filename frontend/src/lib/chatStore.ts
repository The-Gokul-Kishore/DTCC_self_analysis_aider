import { create } from 'zustand';
import { Conversation, ChatMessage } from './types';
import { v4 as uuidv4 } from 'uuid';

interface ChatState {
  conversations: Conversation[];
  selectedConversationId: string | null;
  selectConversation: (id: string) => void;
  addConversation: () => void;
  addMessage: (message: ChatMessage) => void;
}

export const useChatStore = create<ChatState>((set, get) => ({
  conversations: [
    {
      id: uuidv4(),
      title: 'New Chat',
      messages: [],
      createdAt: new Date(),
    },
  ],
  selectedConversationId: null,
  selectConversation: (id) => set({ selectedConversationId: id }),
  addConversation: () =>
    set((state) => {
      const newConv = {
        id: uuidv4(),
        title: 'New Chat',
        messages: [],
        createdAt: new Date(),
      };
      return {
        conversations: [newConv, ...state.conversations],
        selectedConversationId: newConv.id,
      };
    }),
  addMessage: (message) =>
    set((state) => {
      const { selectedConversationId, conversations } = state;
      if (!selectedConversationId) return {};
      return {
        conversations: conversations.map((conv) =>
          conv.id === selectedConversationId
            ? { ...conv, messages: [...conv.messages, message] }
            : conv
        ),
      };
    }),
})); 