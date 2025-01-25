import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';
import express from 'express';

const app = express();
const client = createClient();
const queue = createQueue();
const HOST = '127.0.0.1';
const PORT = 1245;
let reservationEnabled = true;

// Redis client ops
/**
 * Sets the number of available seats from Redis
 * @param {number} number -
 */
function reserveSeat(number) {
  client.set('available_seats', number);
}

/**
 * Queries redis for number of available seats
 * @returns {number} number of available seats
 */
async function getCurrentAvailableSeats() {
  const getAsync = promisify(client.get).bind(client);
  const availableSeats = await getAsync('available_seats');
  return Number(availableSeats);
}

// Express app routes
/* Gets number of available seats */

