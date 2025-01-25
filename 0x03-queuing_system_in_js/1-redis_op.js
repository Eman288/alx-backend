import { print, createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});
redisClient.on('connect', () => console.log('Redis client connected to the server'));

console.log(redisClient.connected);
/**
 * Set a key-value pair in redis
 * @param {string} schoolName - key
 * @param {string} value      - value
 */
function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}


