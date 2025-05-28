import { NextResponse } from 'next/server'
import { MongoClient } from 'mongodb'

const uri = process.env.MONGODB_URI
const client = new MongoClient(uri!)

export async function GET() {
  try {
    await client.connect()
    const database = client.db('chat')
    const messages = database.collection('messages')
    
    const result = await messages.find().sort({ timestamp: 1 }).toArray()
    return NextResponse.json(result)
  } catch (error) {
    console.error('Error fetching messages:', error)
    return NextResponse.json({ error: 'Failed to fetch messages' }, { status: 500 })
  } finally {
    await client.close()
  }
}

export async function POST(request: Request) {
  try {
    const { text, sender } = await request.json()
    
    await client.connect()
    const database = client.db('chat')
    const messages = database.collection('messages')
    
    const message = {
      text,
      sender,
      timestamp: new Date(),
    }
    
    await messages.insertOne(message)
    return NextResponse.json({ success: true })
  } catch (error) {
    console.error('Error sending message:', error)
    return NextResponse.json({ error: 'Failed to send message' }, { status: 500 })
  } finally {
    await client.close()
  }
} 