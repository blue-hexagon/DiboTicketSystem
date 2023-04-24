function currentHourFromDate(date = new Date()) {
    /** @returns {number} - the current hour in a 24-hour format  */
        // Using undefined as the first argument will make the browser use its hosts default locale
    let hours = date.toLocaleString(undefined, {
                hour: 'numeric',
                hour12: false
            }
        ).toString()
    hours = parseInt(hours, 10)
    return hours
}

const ThemeEnum = {
    LIGHT: 'light',
    DARK: 'dark',
    AUTO: 'auto'
}
const ThemeLocalStorage = {
    themeMode: null, /* 'light', 'dark' or 'auto' */
    LS_ITEM: 'themeMode',
    LS_ITEM_SUNRISE: 'themeModeSunrise',
    LS_ITEM_SUNSET: 'themeModeSunset',
    setAutoThemeHoursIfUninitialized: function () {
        if (localStorage.getItem(ThemeLocalStorage.LS_ITEM_SUNRISE) === null || localStorage.getItem(ThemeLocalStorage.LS_ITEM_SUNSET) === null) {
            localStorage.setItem(ThemeLocalStorage.LS_ITEM_SUNRISE, "7");
            localStorage.setItem(ThemeLocalStorage.LS_ITEM_SUNSET, "18");
        }
    },
    getSunrise: function () {
        this.setAutoThemeHoursIfUninitialized()
        return localStorage.getItem(this.LS_ITEM_SUNRISE);
    },
    getSunset: function () {
        this.setAutoThemeHoursIfUninitialized()
        return localStorage.getItem(this.LS_ITEM_SUNSET);
    },
    getTheme: function () {
        try {
            if (localStorage.getItem(this.LS_ITEM) != null) {
                this.themeMode = localStorage.getItem(this.LS_ITEM);
            } else {
                this.themeMode = ThemeEnum.AUTO;
                localStorage.setItem(this.LS_ITEM, ThemeEnum.AUTO);
            }
        } catch (e) {
            /* This catches exceptions thrown on localStorage.setItem
               These can arise when the user or browser denies access to local storage */
            this.themeMode = ThemeEnum.LIGHT;
        }
        if (this.themeMode === ThemeEnum.AUTO) {
            return ThemeController.getAutoTheme();
        }
        return this.themeMode;
    },
    setLightTheme: function () {
        localStorage.setItem(this.LS_ITEM, ThemeEnum.LIGHT)
    },
    setDarkTheme: function () {
        localStorage.setItem(this.LS_ITEM, ThemeEnum.DARK)
    },
    setAutoTheme: function () {
        localStorage.setItem(this.LS_ITEM, ThemeEnum.AUTO)
    },

}


const ThemeController = {
    DATA_ATTRIBUTE_KEY: "data-bs-theme",
    THEME_LS: ThemeLocalStorage,
    getAutoTheme: function (currentHour = currentHourFromDate()) {
        let sunriseHour = this.THEME_LS.getSunrise()
        let sunsetHour = this.THEME_LS.getSunset()
        if (currentHour < sunriseHour || currentHour >= sunsetHour) {
            return ThemeEnum.DARK;
        }
        return ThemeEnum.LIGHT;
    },
    setDarkTheme: function () {
        this.THEME_LS.setDarkTheme();
        this.applyTheme();
    },
    setLightTheme: function () {
        this.THEME_LS.setLightTheme();
        this.applyTheme();
    },
    setAutoTheme: function () {
        this.THEME_LS.setAutoTheme();
        this.applyTheme();
    },
    applyTheme: function () {
        document.getElementsByTagName('html')[0].setAttribute(this.DATA_ATTRIBUTE_KEY, this.THEME_LS.getTheme())
    },
};
module.exports = {
    currentHourFromDate,
    ThemeEnum,
    ThemeLocalStorage,
    ThemeController,
}



