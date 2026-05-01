import { useState } from 'react';
import Form from '../components/Form';
import ResultCard from '../components/ResultCard';

export default function Home() {
  const [result, setResult] = useState(null);
  return (
    <>
      <div className="bg-scene">
        <div className="blob blob-1" />
        <div className="blob blob-2" />
        <div className="grid-lines" />
      </div>
      <main style={{ position: 'relative', zIndex: 1, padding: '2rem 1rem', width: '100%', maxWidth: 560, margin: '0 auto' }}>
        <Form onResult={setResult} />
        <ResultCard data={result} />
      </main>
    </>
  );
}