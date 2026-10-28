/**
 * Unit tests for adapt-abbott-pass-reveal extension.
 *
 * Tests the guard chain and model-answer enabling logic.
 */

import { describe, expect, it, jest, beforeEach, afterEach } from '@jest/globals';

// Global object to capture event handlers - must be declared before jest.mock
// because jest.mock is hoisted but the factory function runs at import time
const registeredHandlers = {};

// Mock Adapt before importing the extension
jest.mock('core/js/adapt', () => {
  const handlers = registeredHandlers;
  return {
    __esModule: true,
    default: {
      on: jest.fn((event, handler) => {
        handlers[event] = handler;
      }),
      course: null,
      assessment: null
    }
  };
});

// Mock logging to prevent console output during tests
jest.mock('core/js/logging', () => ({
  __esModule: true,
  default: {
    debug: jest.fn(),
    info: jest.fn(),
    warn: jest.fn(),
    error: jest.fn()
  }
}));

// Import Adapt after mocking so we can manipulate it
import Adapt from 'core/js/adapt';

// Import the extension to register handlers
import '../../js/adapt-abbott-pass-reveal.js';

beforeEach(() => {
  // Reset Adapt properties before each test
  Adapt.course = null;
  Adapt.assessment = null;
});

afterEach(() => {
  // Clear any mock call history
  jest.clearAllMocks();
});

// Helper to create mock question models
function createMockQuestions(count, initialCanShowModelAnswer = false) {
  const questions = [];
  for (let i = 0; i < count; i++) {
    const data = {
      _id: `q-${i}`,
      _canShowModelAnswer: initialCanShowModelAnswer
    };
    questions.push({
      get: jest.fn(key => data[key]),
      set: jest.fn((key, value) => { data[key] = value; })
    });
  }
  return questions;
}

// Helper to create mock assessment model
function createMockAssessment(questions) {
  return {
    _getAllQuestionComponents: jest.fn(() => questions),
    findDescendantModels: jest.fn(() => questions)
  };
}

// Helper to create mock course with pass-reveal config
function createMockCourse(config) {
  return {
    get: jest.fn(key => {
      if (key === '_passReveal') return config;
      return undefined;
    })
  };
}

describe('adapt-abbott-pass-reveal', () => {

  describe('Guard 1: Extension enabled (inert test)', () => {

    it('should do nothing when _passReveal config is absent', () => {
      // Config absent = no _passReveal key at all
      Adapt.course = createMockCourse(undefined);

      const questions = createMockQuestions(3, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      // Trigger assessments:complete with a passing state
      const handler = registeredHandlers['assessments:complete'];
      expect(handler).toBeDefined();

      handler({ id: 'SUMM-a-01', isPass: true });

      // Model answers should NOT be enabled (extension is inert)
      questions.forEach(q => {
        expect(q.set).not.toHaveBeenCalled();
      });
    });

    it('should do nothing when _passReveal._isEnabled is false', () => {
      Adapt.course = createMockCourse({ _isEnabled: false });

      const questions = createMockQuestions(3, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessments:complete'];
      handler({ id: 'SUMM-a-01', isPass: true });

      // Model answers should NOT be enabled
      questions.forEach(q => {
        expect(q.set).not.toHaveBeenCalled();
      });
    });

    it('should do nothing when _passReveal is empty object', () => {
      Adapt.course = createMockCourse({});

      const questions = createMockQuestions(3, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessments:complete'];
      handler({ id: 'SUMM-a-01', isPass: true });

      // Model answers should NOT be enabled
      questions.forEach(q => {
        expect(q.set).not.toHaveBeenCalled();
      });
    });

  });

  describe('Guard 2: Assessment ID match', () => {

    it('should apply to all assessments when _assessmentIds is not specified', () => {
      Adapt.course = createMockCourse({ _isEnabled: true });

      const questions = createMockQuestions(3, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessments:complete'];
      handler({ id: 'ANY-ASSESSMENT', isPass: true });

      // Model answers SHOULD be enabled (no filter = all assessments)
      questions.forEach(q => {
        expect(q.set).toHaveBeenCalledWith('_canShowModelAnswer', true);
      });
    });

    it('should apply to all assessments when _assessmentIds is empty array', () => {
      Adapt.course = createMockCourse({ _isEnabled: true, _assessmentIds: [] });

      const questions = createMockQuestions(3, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessments:complete'];
      handler({ id: 'ANY-ASSESSMENT', isPass: true });

      // Model answers SHOULD be enabled
      questions.forEach(q => {
        expect(q.set).toHaveBeenCalledWith('_canShowModelAnswer', true);
      });
    });

    it('should apply only to specified assessment IDs', () => {
      Adapt.course = createMockCourse({
        _isEnabled: true,
        _assessmentIds: ['SUMM-a-01']
      });

      const questions = createMockQuestions(3, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessments:complete'];

      // Non-matching assessment should be skipped
      handler({ id: 'OTHER-ASSESSMENT', isPass: true });
      questions.forEach(q => {
        expect(q.set).not.toHaveBeenCalled();
      });

      // Matching assessment should enable model answers
      handler({ id: 'SUMM-a-01', isPass: true });
      questions.forEach(q => {
        expect(q.set).toHaveBeenCalledWith('_canShowModelAnswer', true);
      });
    });

  });

  describe('Guard 3: isPass check', () => {

    it('should NOT enable model answers when isPass is false', () => {
      Adapt.course = createMockCourse({ _isEnabled: true });

      const questions = createMockQuestions(3, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessments:complete'];
      handler({ id: 'SUMM-a-01', isPass: false });

      // Model answers should NOT be enabled
      questions.forEach(q => {
        expect(q.set).not.toHaveBeenCalled();
      });
    });

    it('should enable model answers when isPass is true', () => {
      Adapt.course = createMockCourse({ _isEnabled: true });

      const questions = createMockQuestions(3, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessments:complete'];
      handler({ id: 'SUMM-a-01', isPass: true });

      // Model answers SHOULD be enabled
      questions.forEach(q => {
        expect(q.set).toHaveBeenCalledWith('_canShowModelAnswer', true);
      });
    });

  });

  describe('Event handling', () => {

    it('should register handlers for assessments:complete and assessment:restored', () => {
      // Handlers are registered at module load time, verify they exist
      expect(registeredHandlers['assessments:complete']).toBeDefined();
      expect(registeredHandlers['assessment:restored']).toBeDefined();
    });

    it('should handle assessment:restored the same as assessments:complete', () => {
      Adapt.course = createMockCourse({ _isEnabled: true });

      const questions = createMockQuestions(3, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessment:restored'];
      handler({ id: 'SUMM-a-01', isPass: true });

      // Model answers SHOULD be enabled on restore
      questions.forEach(q => {
        expect(q.set).toHaveBeenCalledWith('_canShowModelAnswer', true);
      });
    });

  });

  describe('Model answer enabling', () => {

    it('should set _canShowModelAnswer to true on all question components', () => {
      Adapt.course = createMockCourse({ _isEnabled: true });

      const questions = createMockQuestions(5, false);
      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessments:complete'];
      handler({ id: 'SUMM-a-01', isPass: true });

      // All 5 questions should have model answers enabled
      expect(questions.length).toBe(5);
      questions.forEach(q => {
        expect(q.set).toHaveBeenCalledWith('_canShowModelAnswer', true);
      });
    });

    it('should not re-set _canShowModelAnswer if already true', () => {
      Adapt.course = createMockCourse({ _isEnabled: true });

      // Create questions where some already have model answer enabled
      const questions = createMockQuestions(3, true);

      Adapt.assessment = {
        get: jest.fn(() => createMockAssessment(questions))
      };

      const handler = registeredHandlers['assessments:complete'];
      handler({ id: 'SUMM-a-01', isPass: true });

      // Questions that already had true should not be re-set
      questions.forEach(q => {
        expect(q.set).not.toHaveBeenCalled();
      });
    });

  });

});
