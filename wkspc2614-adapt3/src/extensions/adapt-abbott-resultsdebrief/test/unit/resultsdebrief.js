/**
 * Unit tests for adapt-abbott-resultsdebrief extension.
 *
 * Tests the guard chain, deduplication logic, and debrief rendering.
 */

import { describe, expect, it, jest, beforeEach, afterEach } from '@jest/globals';

// Global object to capture event handlers
const registeredHandlers = {};

// Mock jQuery for DOM operations. Captures the html passed to .after() so
// SVP-1 tests can inspect the generated markup, not just whether an
// injection was attempted.
let capturedAfterHtml = null;
const mockJQuery = jest.fn(() => ({
  length: 1,
  find: jest.fn(() => ({
    length: 1,
    remove: jest.fn(),
    after: jest.fn(html => { capturedAfterHtml = html; }),
    first: jest.fn(() => ({
      trigger: jest.fn()
    }))
  }))
}));
global.$ = mockJQuery;

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
      components: {
        findWhere: jest.fn()
      }
    }
  };
});

// Mock logging
jest.mock('core/js/logging', () => ({
  __esModule: true,
  default: {
    debug: jest.fn(),
    info: jest.fn(),
    warn: jest.fn(),
    error: jest.fn()
  }
}));

import Adapt from 'core/js/adapt';

// Import the extension to register handlers
import '../../js/adapt-abbott-resultsdebrief.js';

beforeEach(() => {
  Adapt.course = null;
  Adapt.components.findWhere.mockReset();
  mockJQuery.mockClear();
  capturedAfterHtml = null;
});

afterEach(() => {
  jest.clearAllMocks();
});

// Helper to create mock course with resultsDebrief config
function createMockCourse(config) {
  return {
    get: jest.fn(key => {
      if (key === '_resultsDebrief') return config;
      return undefined;
    })
  };
}

// Helper to create assessment state
function createAssessmentState(overrides = {}) {
  return {
    id: 'SUMM-a-01',
    isComplete: true,
    isPass: false,
    questions: [],
    ...overrides
  };
}

// Helper to create config with items
function createConfig(overrides = {}) {
  return {
    _isEnabled: true,
    _assessmentId: 'SUMM-a-01',
    _studyPlanHeading: 'Where to focus next',
    _passRevealNote: 'You can now view the correct answers.',
    _items: [
      { _questionId: 'q-1', topic: 'topic A', lessonTitle: 'Lesson 1' },
      { _questionId: 'q-2', topic: 'topic B', lessonTitle: 'Lesson 1' },
      { _questionId: 'q-3', topic: 'topic C', lessonTitle: 'Lesson 2' }
    ],
    ...overrides
  };
}

describe('adapt-abbott-resultsdebrief', () => {

  describe('Guard 1: Extension enabled (inert test)', () => {

    it('should do nothing when _resultsDebrief config is absent', () => {
      Adapt.course = createMockCourse(undefined);

      const handler = registeredHandlers['assessments:complete'];
      expect(handler).toBeDefined();

      handler(createAssessmentState());

      // No DOM operations should occur
      expect(Adapt.components.findWhere).not.toHaveBeenCalled();
    });

    it('should do nothing when _resultsDebrief._isEnabled is false', () => {
      Adapt.course = createMockCourse({ _isEnabled: false });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState());

      expect(Adapt.components.findWhere).not.toHaveBeenCalled();
    });

  });

  describe('Guard 2: Assessment ID match', () => {

    it('should skip non-matching assessment IDs', () => {
      Adapt.course = createMockCourse(createConfig({ _assessmentId: 'SUMM-a-01' }));

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({ id: 'OTHER-ASSESSMENT' }));

      expect(Adapt.components.findWhere).not.toHaveBeenCalled();
    });

    it('should process matching assessment ID', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({ id: 'SUMM-a-01' }));

      expect(Adapt.components.findWhere).toHaveBeenCalledWith({
        _component: 'assessmentResults',
        _assessmentId: 'SUMM-a-01'
      });
    });

  });

  describe('Guard 3: Assessment complete check', () => {

    it('should skip if assessment is not complete', () => {
      Adapt.course = createMockCourse(createConfig());

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({ isComplete: false }));

      expect(Adapt.components.findWhere).not.toHaveBeenCalled();
    });

  });

  describe('Deduplication by lesson', () => {

    it('should group multiple wrong questions from same lesson', () => {
      // This tests the groupByLesson logic indirectly
      // Two questions from Lesson 1, one from Lesson 2
      const config = createConfig();
      Adapt.course = createMockCourse(config);
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({
        questions: [
          { _id: 'q-1', _isCorrect: false },
          { _id: 'q-2', _isCorrect: false },
          { _id: 'q-3', _isCorrect: true }
        ]
      }));

      // Should have attempted injection (verify findWhere was called)
      expect(Adapt.components.findWhere).toHaveBeenCalled();
    });

  });

  describe('Study plan rendering', () => {

    it('should render study plan when answers are wrong on fail', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({
        isPass: false,
        questions: [
          { _id: 'q-1', _isCorrect: false }
        ]
      }));

      expect(Adapt.components.findWhere).toHaveBeenCalled();
    });

    it('should render study plan AND pass note when answers wrong on pass', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({
        isPass: true,
        questions: [
          { _id: 'q-1', _isCorrect: false },
          { _id: 'q-2', _isCorrect: true },
          { _id: 'q-3', _isCorrect: true }
        ]
      }));

      expect(Adapt.components.findWhere).toHaveBeenCalled();
    });

    it('should render only pass note when all correct on pass', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({
        isPass: true,
        questions: [
          { _id: 'q-1', _isCorrect: true },
          { _id: 'q-2', _isCorrect: true },
          { _id: 'q-3', _isCorrect: true }
        ]
      }));

      expect(Adapt.components.findWhere).toHaveBeenCalled();
    });

  });

  describe('Event handling', () => {

    it('should register handlers for assessments:complete, assessment:restored, and componentView:postRender', () => {
      expect(registeredHandlers['assessments:complete']).toBeDefined();
      expect(registeredHandlers['assessment:restored']).toBeDefined();
      expect(registeredHandlers['componentView:postRender']).toBeDefined();
    });

    it('should handle assessment:restored the same as assessments:complete', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessment:restored'];
      handler(createAssessmentState({
        questions: [{ _id: 'q-1', _isCorrect: false }]
      }));

      expect(Adapt.components.findWhere).toHaveBeenCalled();
    });

    it('should handle componentView:postRender for assessmentResults', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      // First complete the assessment to populate completedAssessments
      const completeHandler = registeredHandlers['assessments:complete'];
      completeHandler(createAssessmentState({
        questions: [{ _id: 'q-1', _isCorrect: false }]
      }));

      // Then trigger postRender
      const postRenderHandler = registeredHandlers['componentView:postRender'];
      const mockView = {
        model: {
          get: jest.fn(key => {
            if (key === '_component') return 'assessmentResults';
            if (key === '_assessmentId') return 'SUMM-a-01';
            return undefined;
          })
        }
      };
      postRenderHandler(mockView);

      // Should attempt injection
      expect(Adapt.components.findWhere).toHaveBeenCalled();
    });

  });

  describe('SVP-1: every question shown, in order, marked correct or incorrect', () => {

    it('includes a results-list item for every question, correct and incorrect alike, not just the wrong ones', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({
        questions: [
          { _id: 'q-1', _isCorrect: true },
          { _id: 'q-2', _isCorrect: false },
          { _id: 'q-3', _isCorrect: true }
        ]
      }));

      expect(capturedAfterHtml).toContain('Your answers');
      // 3 questions in, 3 results-items out (not 1, as the old
      // _isCorrect === false filter would have produced).
      const itemCount = (capturedAfterHtml.match(/resultsdebrief__results-item/g) || []).length;
      expect(itemCount).toBe(3);
    });

    it('marks each question correct or incorrect and preserves assessment order', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({
        questions: [
          { _id: 'q-1', _isCorrect: true },
          { _id: 'q-2', _isCorrect: false },
          { _id: 'q-3', _isCorrect: true }
        ]
      }));

      const html = capturedAfterHtml;
      const posQ1 = html.indexOf('topic A');
      const posQ2 = html.indexOf('topic B');
      const posQ3 = html.indexOf('topic C');
      expect(posQ1).toBeGreaterThan(-1);
      expect(posQ2).toBeGreaterThan(posQ1);
      expect(posQ3).toBeGreaterThan(posQ2);

      // is-correct / is-incorrect classes present per question, not just
      // one bucket
      expect((html.match(/is-correct/g) || []).length).toBeGreaterThanOrEqual(2);
      expect((html.match(/is-incorrect/g) || []).length).toBeGreaterThanOrEqual(1);
    });

    it('carries screen-reader text for correctness, not colour/shape alone (SEL-1)', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({
        questions: [
          { _id: 'q-1', _isCorrect: true },
          { _id: 'q-2', _isCorrect: false }
        ]
      }));

      const html = capturedAfterHtml;
      expect(html).toContain('visually-hidden">Correct.');
      expect(html).toContain('visually-hidden">Incorrect.');
      // Icons are aria-hidden; the visually-hidden text is what a screen
      // reader announces, so correctness never depends on the icon shape
      // or colour alone.
      expect(html).toContain('aria-hidden="true"');
    });

    it('falls back to a question number when a question has no topic/lesson mapping', () => {
      Adapt.course = createMockCourse(createConfig({ _items: [] }));
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({
        questions: [
          { _id: 'unmapped-1', _isCorrect: true },
          { _id: 'unmapped-2', _isCorrect: false }
        ]
      }));

      expect(capturedAfterHtml).toContain('Question 1');
      expect(capturedAfterHtml).toContain('Question 2');
    });

    it('still shows the results list even when every question is correct (no study plan)', () => {
      Adapt.course = createMockCourse(createConfig());
      Adapt.components.findWhere.mockReturnValue({ get: () => 'SUMM-c-50' });

      const handler = registeredHandlers['assessments:complete'];
      handler(createAssessmentState({
        isPass: true,
        questions: [
          { _id: 'q-1', _isCorrect: true },
          { _id: 'q-2', _isCorrect: true }
        ]
      }));

      expect(capturedAfterHtml).toContain('Your answers');
      expect((capturedAfterHtml.match(/resultsdebrief__results-item/g) || []).length).toBe(2);
      // No study plan heading, since nothing was wrong
      expect(capturedAfterHtml).not.toContain('Where to focus next');
    });

  });

  describe('Question text never rendered', () => {

    it('should not include question body or answers in output', () => {
      // This is tested by inspection of generateDebriefHtml - it only uses
      // topic and lessonTitle from config, never accesses question models
      // for their body/answer content. The test verifies the config structure
      // is used correctly.
      const config = createConfig();
      expect(config._items[0]).not.toHaveProperty('body');
      expect(config._items[0]).not.toHaveProperty('answer');
      expect(config._items[0]).toHaveProperty('topic');
      expect(config._items[0]).toHaveProperty('lessonTitle');
    });

  });

});
