const path = require("path")
const BundleTracker = require('webpack-bundle-tracker')
const MiniCssExtractPlugin = require("mini-css-extract-plugin")

// check if we are running in production, make sure you use the same env var for both django and webpack
// const isDevelopment = (process.env.DEBUG || "false").toLowerCase() == "true";
const isDevelopment = true

module.exports = [
    {
        target: ['web', 'es5'],
        context: path.resolve(),
        mode: isDevelopment ? "development" : "production",
        entry: {
            main_style: './assets/main.scss',
            main_js: './assets/main.js'
        },
        output: {
            path: path.resolve('./assets/webpack_bundles/'),
            filename: "[name]-[fullhash].js",
            clean: true,
            publicPath: isDevelopment ? 'http://localhost:8001/' : undefined,
        },
        devServer: {
            port: 8001,
            headers: {
                "Access-Control-Allow-Origin": "*",
            }
        },
        devtool: isDevelopment ? "eval" : "source-map",
        plugins: [
            new BundleTracker({filename: './webpack-stats.json'}),
            new MiniCssExtractPlugin({
                filename: "[name]-[fullhash].css",
                chunkFilename: "[id]-[fullhash].css",
            }),
        ],
        module: {
            rules: [

                {
                    test: /\.m?js$/,
                    exclude: /(node_modules|bower_components)/,
                    use: {
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env']
                        }
                    }
                },
                {
                    test: /\.s[ac]ss$/i,
                    use: [
                        isDevelopment ? "style-loader" : MiniCssExtractPlugin.loader,
                        {
                            loader: 'css-loader',
                            options: {
                                sourceMap: isDevelopment
                            }
                        },
                        {
                            loader: 'sass-loader',
                            options: {
                                sourceMap: isDevelopment
                            }
                        },
                    ],
                },
                {
                    test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
                    type: 'asset',
                    generator: {
                        filename: 'fonts/en/[hash][ext][query]',
                    },
                },
                {
                    test: /\.(png|jpe?g|gif)$/i,
                    use: [
                        {
                            loader: "file-loader",
                            options: {
                                name: "images/[name].[ext]"
                            }
                        }
                    ]
                }
            ]
        }
    }
]