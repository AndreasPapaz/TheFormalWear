// let webpack = require('webpack');
module.exports = {

  // This code will be compiled
  entry: "./app/app.js",
  // entry: ".test/bundle.js",

  // Then output into this file
  output: {
    // filename: "public/bundle.js"
    filename: "./assets/bundles/bundle.js"
  },

  // This will be what we do
    module: {
    rules: [
      {
        test: /\.jsx?$/,
        // only process files in app folder
        include: /app/,
        loader: 'babel-loader',
        query: {
          // transformations
          presets: ['@babel/react'],
          plugins: ['@babel/proposal-class-properties']
        }
      }
    ]
  }
}
