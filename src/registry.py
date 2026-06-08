"""Single source of truth mapping each PAGES fname to its lesson function."""

import part1
import part2
import part3
import part4
import part5
import glossary

CONTENT = {
    "01-what-is-ga.html": part1.lesson_01,
    "02-project-map.html": part1.lesson_02,
    "03-task-lifecycle.html": part1.lesson_03,
    "04-install.html": part2.lesson_04,
    "05-frontends.html": part2.lesson_05,
    "06-commands.html": part2.lesson_06,
    "07-tools.html": part2.lesson_07,
    "08-agent-loop.html": part3.lesson_08,
    "09-llmcore.html": part3.lesson_09,
    "10-handler-dispatch.html": part3.lesson_10,
    "11-layered-memory.html": part3.lesson_11,
    "12-memory-crystallize.html": part3.lesson_12,
    "13-hooks-observability.html": part3.lesson_13,
    "14-rendering.html": part3.lesson_14,
    "15-vision.html": part4.lesson_15,
    "16-input-mobile.html": part4.lesson_16,
    "17-browser.html": part4.lesson_17,
    "18-reflect-orchestration.html": part4.lesson_18,
    "19-autonomy.html": part4.lesson_19,
    "20-self-evolution.html": part5.lesson_20,
    "21-build-a-skill.html": part5.lesson_21,
    "22-extend-frontend.html": part5.lesson_22,
    "23-glossary.html": glossary.lesson_23,
}
