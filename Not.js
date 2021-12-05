const fetch = require("node-fetch");

const pluginRss = require("@11ty/eleventy-plugin-rss");

// docs: https://www.11ty.io/docs/config/

module.exports = function(eleventyConfig) {

  eleventyConfig.addPlugin(pluginRss);

  eleventyConfig.addPassthroughCopy("css");

  eleventyConfig.addCollection("posts", collection => {

    return [...collection.getFilteredByGlob("./src/**/*.md")]

      .filter(p => !p.data.draft)

      .reverse();

  });

  return {

    passthroughFileCopy: true,

    pathPrefix: "/veil-look",

    dir: {

      input: "src",

      output: "docs"

    }

  };

};
