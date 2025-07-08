import { Editor } from 'https://esm.sh/@tiptap/core';
import StarterKit from 'https://esm.sh/@tiptap/starter-kit';
import Placeholder from 'https://esm.sh/@tiptap/extension-placeholder';
import Paragraph from 'https://esm.sh/@tiptap/extension-paragraph';
import Bold from 'https://esm.sh/@tiptap/extension-bold';
import Underline from 'https://esm.sh/@tiptap/extension-underline';
import Link from 'https://esm.sh/@tiptap/extension-link';
import BulletList from 'https://esm.sh/@tiptap/extension-bullet-list';
import OrderedList from 'https://esm.sh/@tiptap/extension-ordered-list';
import Blockquote from 'https://esm.sh/@tiptap/extension-blockquote';

document.addEventListener("DOMContentLoaded", () => {
  // Explicitly target the content field
  const contentInput = document.getElementById("id_content");
  if (!contentInput) {
    console.error("Content input field not found");
    return;
  }

  const editor = new Editor({
    element: document.querySelector("#hs-editor-tiptap [data-hs-editor-field]"),
    content: contentInput.value || "",
    extensions: [
      StarterKit,
      Placeholder.configure({ placeholder: "Write your blog content..." }),
      Paragraph,
      Bold,
      Underline,
      Link.configure({
        openOnClick: false,
        HTMLAttributes: {
          target: "_blank",
          rel: "noopener noreferrer",
        },
      }),
      BulletList,
      OrderedList,
      Blockquote,
    ],
    onUpdate: ({ editor }) => {
      contentInput.value = editor.getHTML();
    },
  });

  const actions = [
    {
      id: "[data-hs-editor-bold]",
      fn: () => editor.chain().focus().toggleBold().run(),
    },
    {
      id: "[data-hs-editor-italic]",
      fn: () => editor.chain().focus().toggleItalic().run(),
    },
    {
      id: "[data-hs-editor-underline]",
      fn: () => editor.chain().focus().toggleUnderline().run(),
    },
    {
      id: "[data-hs-editor-strike]",
      fn: () => editor.chain().focus().toggleStrike().run(),
    },
    {
      id: "[data-hs-editor-link]",
      fn: () => {
        const url = window.prompt("Enter URL:");
        if (url) {
          // Validate URL
          try {
            new URL(url);
            editor
              .chain()
              .focus()
              .extendMarkRange("link")
              .setLink({ href: url })
              .run();
          } catch {
            alert("Please enter a valid URL.");
          }
        }
      },
    },
    {
      id: "[data-hs-editor-ol]",
      fn: () => editor.chain().focus().toggleOrderedList().run(),
    },
    {
      id: "[data-hs-editor-ul]",
      fn: () => editor.chain().focus().toggleBulletList().run(),
    },
    {
      id: "[data-hs-editor-code]",
      fn: () => editor.chain().focus().toggleCode().run(),
    },
  ];

  actions.forEach(({ id, fn }) => {
    const btn = document.querySelector(id);
    if (btn) {
      btn.addEventListener("click", fn);
    } else {
      console.warn(`Button ${id} not found`);
    }
  });

  // Prevent form submit if empty
  const form = document.getElementById("blog-form");
  form?.addEventListener("submit", (e) => {
    const plainText = editor.getText().trim();
    if (plainText.length === 0) {
      e.preventDefault();
      document.getElementById("content-error").classList.remove("hidden");
    }
  });
});
