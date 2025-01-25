import { createQueue } from 'kue';
import { expect } from 'chai';
import { spy } from 'sinon';
import createPushNotificationsJobs from './8-jobs';

// Job  creation unit tests
describe('createPushNotifications unit tests', () => {
  const queue = createQueue();
  before(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  after(() => {
    queue.testMode.exit();
  });

