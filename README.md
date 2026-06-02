# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

## Run the demo

1. Open a terminal in the project folder:

```bash
cd /Users/shocka/Future-Plan-Scenario
```

2. Install dependencies:

```bash
npm install
```

3. Start the dashboard (auto-opens browser):

```bash
npm start
```

4. Open the URL shown in the terminal (typically `http://localhost:5173/`).

5. Stop the server when done with `Ctrl + C`.

## One-click launch on macOS

If you prefer, you can start everything by double-clicking `start.command` in Finder.
This script will:

- install dependencies if needed
- start the Vite server
- open the dashboard in your browser

## Optional: production preview

1. Build the app:

```bash
npm run build
```

2. Start preview server:

```bash
npm run preview
```

3. Open the preview URL shown in terminal (typically `http://localhost:4173/`).

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
