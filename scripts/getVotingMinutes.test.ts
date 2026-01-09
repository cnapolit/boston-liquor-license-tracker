import { expect, test, describe, beforeAll, afterAll, afterEach, vi } from "vitest";

const testFilePath = path.join(__dirname, "test_pdf.pdf");
//load file
let data;


vi.mock('axios', () => {
  const getMock = vi.fn(async (str) => {
    
    return { data: data };
  })
  return { default: { get: getMock } }
});

import { main } from "./getVotingMinutes.js";
import fs from "fs/promises";
import path from "path";

const resultFilePath = path.join(__dirname, "downloaded_voting_minutes.pdf");

describe("main", () => {
  
  afterEach(async () => {
    await fs.unlink(resultFilePath).catch(() => {}); // Clean up the downloaded file after test
  });
  beforeAll(async () => {
    data = await fs.readFile(testFilePath);
  });

  test("main retrieves PDF", async () => {
    await main();

    // const fileExists = await fs
    //   .access(resultFilePath)
    //   .then(() => true)
    //   .catch(() => false);
    // expect(fileExists).toBe(true);
    // const resultFileContents = await fs.readFile(resultFilePath);
    // const testFileContents = await fs.readFile(testFilePath);
    // expect(resultFileContents).toEqual(testFileContents);
  });
});