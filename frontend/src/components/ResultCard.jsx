export default function ResultCard({ data }) {
  if (!data) return null;
  const { price, low, high } = data;
  return (
    <div className="result-box">
      <p className="result-lbl">Estimated monthly rent</p>
      <p className="result-price">¥ {price.toLocaleString()} / mo</p>
      <p className="result-range">Range ¥{low.toLocaleString()} – ¥{high.toLocaleString()}</p>
    </div>
  );
}