'use client';

import Link from 'next/link';
import MotionWrapper from '@/components/MotionWrapper';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-gray-900 text-white">
      <div className="container mx-auto px-4 py-16">
        <MotionWrapper
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-center"
        >
          <h1 className="text-6xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
            Into the Unknown
          </h1>
          <p className="text-xl mb-12 text-gray-300 max-w-2xl mx-auto">
            Embark on a journey through the depths of artificial intelligence. 
            Discover insights, explore possibilities, and unlock the mysteries of tomorrow.
          </p>
          
          <MotionWrapper
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5 }}
            className="space-x-6"
          >
            <Link 
              href="/login"
              className="inline-block px-8 py-3 bg-purple-600 hover:bg-purple-700 rounded-lg font-semibold transition-colors"
            >
              Begin Journey
            </Link>
            <Link
              href="/signup"
              className="inline-block px-8 py-3 border border-purple-600 hover:bg-purple-600/20 rounded-lg font-semibold transition-colors"
            >
              Create Account
            </Link>
          </MotionWrapper>
        </MotionWrapper>

        <MotionWrapper
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
          className="mt-24 grid grid-cols-1 md:grid-cols-3 gap-8"
        >
          {[
            {
              title: "Intelligent Conversations",
              description: "Engage in meaningful dialogues with our advanced AI"
            },
            {
              title: "Deep Insights",
              description: "Uncover hidden patterns and valuable information"
            },
            {
              title: "Continuous Learning",
              description: "Experience an AI that grows with every interaction"
            }
          ].map((feature, index) => (
            <MotionWrapper
              key={index}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 1.2 + index * 0.2 }}
              className="p-6 rounded-xl bg-purple-900/30 backdrop-blur-sm border border-purple-500/20"
            >
              <h3 className="text-xl font-semibold mb-3">{feature.title}</h3>
              <p className="text-gray-400">{feature.description}</p>
            </MotionWrapper>
          ))}
        </MotionWrapper>
      </div>
    </div>
  );
} 