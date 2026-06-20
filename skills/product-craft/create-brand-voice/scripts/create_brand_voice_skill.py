#!/usr/bin/env python3
"""Create a local product-specific brand voice skill."""

from __future__ import annotations

import argparse
import os
import re
import textwrap
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "brand"


def split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def ask(prompt: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    answer = input(f"{prompt}{suffix}: ").strip()
    return answer or (default or "")


def ask_list(prompt: str, default: str | None = None) -> list[str]:
    value = ask(prompt, default)
    return split_csv(value)


def bullet_list(items: list[str], fallback: str = "TODO") -> str:
    if not items:
        return f"- {fallback}"
    return "\n".join(f"- {item}" for item in items)


def paragraph(value: str | None, fallback: str = "TODO") -> str:
    cleaned = (value or "").strip()
    return cleaned or fallback


def yaml_quote(value: str) -> str:
    cleaned = " ".join(value.split())
    escaped = cleaned.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def default_output_dir() -> Path:
    agent_skills_home = os.environ.get("AGENT_SKILLS_HOME")
    if agent_skills_home:
        return Path(agent_skills_home).expanduser()
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "skills"
    return Path.home() / ".codex" / "skills"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a local product-specific brand voice skill."
    )
    parser.add_argument("--name", help="Brand, product, project, or person name.")
    parser.add_argument("--slug", help="Skill slug. Defaults to <name>-brand-voice.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=default_output_dir(),
        help="Directory that will receive the generated skill folder.",
    )
    parser.add_argument(
        "--website-url",
        action="append",
        default=[],
        help="Website, docs, blog, social, or competitor URL. Repeat as needed.",
    )
    parser.add_argument("--audience", help="Primary audience, user, or buyer.")
    parser.add_argument("--category", help="Product category or market frame.")
    parser.add_argument(
        "--tone",
        help="Comma-separated tone descriptors, such as clear, practical, warm.",
    )
    parser.add_argument("--avoid", help="Comma-separated words, phrases, or habits to avoid.")
    parser.add_argument(
        "--surfaces",
        help="Comma-separated surfaces, such as website, docs, UI copy, emails.",
    )
    parser.add_argument(
        "--differentiation",
        help="What makes this brand or product meaningfully different.",
    )
    parser.add_argument(
        "--example",
        action="append",
        default=[],
        help="Safe example copy path or URL. Repeat as needed.",
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Do not prompt. Missing fields become TODOs.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing generated skill folder.",
    )
    return parser.parse_args()


def collect_inputs(args: argparse.Namespace) -> dict[str, object]:
    if not args.non_interactive:
        args.name = args.name or ask("Brand, product, project, or person name")
        if not args.website_url:
            urls = ask_list("URLs to inspect later, comma-separated", "")
            args.website_url = urls
        args.audience = args.audience or ask("Primary audience or buyer", "")
        args.category = args.category or ask("Product category or market frame", "")
        args.tone = args.tone or ask("Desired tone descriptors, comma-separated", "")
        args.avoid = args.avoid or ask("Words, claims, or habits to avoid, comma-separated", "")
        args.surfaces = args.surfaces or ask("Surfaces covered, comma-separated", "")
        args.differentiation = args.differentiation or ask(
            "Meaningful differentiation or positioning notes", ""
        )
        if not args.example:
            args.example = ask_list("Safe example copy paths or URLs, comma-separated", "")

    name = paragraph(args.name, "TODO Brand")
    slug = args.slug or f"{slugify(name)}-brand-voice"

    return {
        "name": name,
        "slug": slugify(slug),
        "urls": args.website_url,
        "audience": args.audience or "",
        "category": args.category or "",
        "tone": split_csv(args.tone),
        "avoid": split_csv(args.avoid),
        "surfaces": split_csv(args.surfaces),
        "differentiation": args.differentiation or "",
        "examples": args.example,
    }


def render_skill_md(data: dict[str, object]) -> str:
    name = str(data["name"])
    slug = str(data["slug"])
    surfaces = data["surfaces"]
    surface_text = ", ".join(surfaces) if isinstance(surfaces, list) and surfaces else "customer-facing copy"
    return textwrap.dedent(
        f"""\
        ---
        name: {slug}
        description: {yaml_quote(f"Brand voice guidance for {name}. Use when drafting, rewriting, reviewing, or editing {surface_text} for {name}.")}
        ---

        # {name} Brand Voice

        Use this skill when writing, rewriting, or reviewing copy for {name}.

        ## Core Workflow

        1. Identify the surface: website, docs, product UI, onboarding, lifecycle email, sales message, social post, support reply, error state, release note, or ad.
        2. Read `references/brand-voice.md` before drafting or editing.
        3. If current product facts matter, inspect the listed public URLs before making claims.
        4. Preserve the audience and category frame. Do not introduce unsupported promises.
        5. Draft in the brand voice, then run the copy checks before returning.

        ## Copy Checks

        - Is the audience specific?
        - Is the claim concrete and supported?
        - Does the copy avoid forbidden words, habits, and vague hype?
        - Does the copy read like finished public-facing writing instead of internal reasoning?
        - Does the surface get the right amount of detail?
        - Would a user know the next action without reading extra explanation?
        - Are private facts, secrets, customer names, process notes, and implementation details excluded?

        ## Output Guidance

        For rewrites, provide the improved copy first, then a short note naming the important changes.
        For reviews, lead with actionable issues ordered by severity.
        For new drafts, include assumptions when product facts are incomplete.
        Do not include internal thought, prompt interpretation, or process narration in the copy itself.
        """
    )


def render_reference_md(data: dict[str, object]) -> str:
    name = str(data["name"])
    urls = data["urls"] if isinstance(data["urls"], list) else []
    tone = data["tone"] if isinstance(data["tone"], list) else []
    avoid = data["avoid"] if isinstance(data["avoid"], list) else []
    surfaces = data["surfaces"] if isinstance(data["surfaces"], list) else []
    examples = data["examples"] if isinstance(data["examples"], list) else []

    return f"""# {name} Brand Voice Reference

## Public Sources To Inspect

{bullet_list(urls, "TODO: add public website, docs, blog, social, or competitor URLs")}

## Audience

{paragraph(str(data["audience"]))}

## Category Frame

{paragraph(str(data["category"]))}

## Differentiation

{paragraph(str(data["differentiation"]))}

## Tone

{bullet_list(tone, "TODO: add concrete tone descriptors")}

Translate tone adjectives into observable choices: sentence length, vocabulary, proof level, humor level, directness, and amount of technical detail.

## Vocabulary To Prefer

- TODO: add product-specific nouns, verbs, and phrases that sound true for this brand.

## Avoid

{bullet_list(avoid, "TODO: add words, claims, phrases, and habits to avoid")}

Also avoid unsupported superlatives, vague AI claims, fake urgency, internal reasoning, process notes, prompt interpretation, private implementation details, customer names, secrets, credentials, and personal local paths.

## Public-Facing Writing Rule

Write for the reader, not the writer. The final copy should not reveal internal thought, agent reasoning, draft notes, review commentary, or implementation process unless the user explicitly asks for that explanation.

## Surface Guidance

{bullet_list(surfaces, "TODO: add covered surfaces such as website, docs, UI, emails, social")}

For each surface, define the job of the copy, ideal length, call to action, and evidence level.

## Safe Examples

{bullet_list(examples, "TODO: add safe examples or links")}

## Before And After Patterns

- TODO: add examples of weak copy and stronger brand-voice rewrites.

## Open Questions

- TODO: add missing facts that future agents should ask before making strong claims.
"""


def write_skill(output_dir: Path, data: dict[str, object], force: bool) -> Path:
    skill_dir = output_dir.expanduser() / str(data["slug"])
    references_dir = skill_dir / "references"

    if skill_dir.exists() and not force:
        raise SystemExit(f"Refusing to overwrite existing skill: {skill_dir}")

    references_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(render_skill_md(data), encoding="utf-8")
    (references_dir / "brand-voice.md").write_text(
        render_reference_md(data), encoding="utf-8"
    )
    return skill_dir


def main() -> None:
    args = parse_args()
    data = collect_inputs(args)
    skill_dir = write_skill(args.output_dir, data, args.force)
    print(f"Created brand voice skill: {skill_dir}")
    print(f"Skill name: {data['slug']}")


if __name__ == "__main__":
    main()
