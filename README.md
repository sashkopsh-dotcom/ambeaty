# AM Beauty Concept

Статический сайт на французском языке. Публичные файлы находятся в `dist/`.

Локальный просмотр: `npm run dev`. Проверка: `npm run check`.
Установка зависимостей и сборка не требуются; нужны Python 3 и Node.js 18+.

## GitHub Pages

1. В репозитории `sashkopsh-dotcom/ambeaty` открыть **Settings → Pages**.
2. В **Build and deployment → Source** выбрать **GitHub Actions**.
3. Отправить изменения в `main`. Workflow `.github/workflows/pages.yml`
   проверит сайт и опубликует только содержимое `dist/`.
4. Дождаться успешного workflow **Deploy to GitHub Pages** во вкладке **Actions**.
   Если изменения уже отправлены, запустить его через **Run workflow → main**.

Ожидаемый адрес после успешного размещения:
https://sashkopsh-dotcom.github.io/ambeaty/

Ресурсы используют относительные адреса, совместимые с префиксом `/ambeaty/`.
Секреты для публикации добавлять не требуется: используется встроенный `GITHUB_TOKEN`.

Артефакт получает отдельное имя для каждого запуска и попытки: `github-pages-<run_id>-<run_attempt>`.
Upload и Deploy используют одно и то же имя, чтобы повтор задания не выбирал старые артефакты.
После изменения workflow запускать новую версию через push или **Run workflow**;
повтор старого запуска использует старую версию workflow.

Это размещение текущего макета. Временный `noindex, nofollow` сохранен;
незавершенные проверки и сведения для окончательного выпуска перечислены в
[плане](DEVELOPMENT_PLAN.md) и [проектной документации](PROJECT_DOCUMENTATION.md).
