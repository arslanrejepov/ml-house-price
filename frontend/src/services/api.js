import axios from 'axios';

export async function predictRent(params) {
  const { data } = await axios.post('/api/predict', params);
  return data; // expects { price, low, high }
}