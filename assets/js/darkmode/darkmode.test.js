import {describe, expect} from '@jest/globals';
import {currentHourFromDate, ThemeController, ThemeEnum, ThemeLocalStorage} from "./darkmode";
import {LocalStorageMock} from "./localStorageMock";

function getHour(hours, minutes, seconds = 0) {
    let testHour = new Date();
    testHour.setHours(hours, minutes, seconds);
    return currentHourFromDate(testHour)
}

describe('ThemeController', () => {
    test(`ThemeController.getAutoTheme() returns dark when clock is 00:00`, () => {
        const testHour = getHour(0, 0);
        expect(ThemeController.getAutoTheme(testHour)).toBe(ThemeEnum.DARK);
    });
    test(`ThemeController.getAutoTheme() returns dark when clock is ${ThemeLocalStorage.getSunrise() - 1}:59`, () => {
        const testHour = getHour(ThemeLocalStorage.getSunrise() - 1, 59);
        expect(ThemeController.getAutoTheme(testHour)).toBe(ThemeEnum.DARK);
    });

    test(`ThemeController.getAutoTheme() returns light when clock is ${ThemeLocalStorage.getSunrise()}:00`, () => {
        const testHour = getHour(ThemeLocalStorage.getSunrise(), 0);
        expect(ThemeController.getAutoTheme(testHour)).toBe(ThemeEnum.LIGHT);
    });
    test(`ThemeController.getAutoTheme() returns light when clock is ${ThemeLocalStorage.getSunset() - 1}:59`, () => {
        const testHour = getHour(ThemeLocalStorage.getSunset() - 1, 59);
        expect(ThemeController.getAutoTheme(testHour)).toBe(ThemeEnum.LIGHT);
    });

    test(`ThemeController.getAutoTheme() returns dark when clock is ${ThemeLocalStorage.getSunset()}:00`, () => {
        const testHour = getHour(ThemeLocalStorage.getSunset(), 0);
        expect(ThemeController.getAutoTheme(testHour)).toBe(ThemeEnum.DARK);
    });
    test(`ThemeController.getAutoTheme() returns dark when clock is 23:59`, () => {
        const testHour = getHour(23, 59);
        expect(ThemeController.getAutoTheme(testHour)).toBe(ThemeEnum.DARK);
    });
})