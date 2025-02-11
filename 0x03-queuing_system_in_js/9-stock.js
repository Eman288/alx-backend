import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();
const HOST = '127.0.0.1';
const PORT = 1245;
const listProducts = [{
  id: 1, name: 'Suitcase 250', price: 50, stock: 4,
},
{
  id: 2, name: 'Suitcase 450', price: 100, stock: 10,
},
{
  id: 3, name: 'Suitcase 650', price: 350, stock: 2,
},
{
  id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
},
];

/**
 * Searches for product in listProducts based on id parameter
 * @param {number} id - product's id

