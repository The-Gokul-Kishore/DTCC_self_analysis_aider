import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getAnalytics } from 'firebase/analytics';

const firebaseConfig = {
  apiKey: "AIzaSyAZFBz30BGUo7lnAFgMTTGvUwQFCxJ5ZpU",
  authDomain: "dtcc-9f28e.firebaseapp.com",
  projectId: "dtcc-9f28e",
  storageBucket: "dtcc-9f28e.appspot.com",
  messagingSenderId: "922867227301",
  appId: "1:922867227301:web:18f0ee01dcad969bbe8b4c",
  measurementId: "G-NLDLCFBLCQ"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const analytics = getAnalytics(app);
export default app; 
