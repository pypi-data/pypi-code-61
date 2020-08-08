# Generated by Django 3.0.7 on 2020-07-27 22:32

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks
import webspace.cms.blocks.static.social_links
import webspace.cms.blocks.static.social_share


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20200724_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='webspacesettings',
            name='brand_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='webspacesettings',
            name='brand_short_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='webspacesettings',
            name='primary_bg_color',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='webspacesettings',
            name='primary_color_uks',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.core.fields.StreamField([('svg', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('svg', wagtail.core.blocks.StructBlock([('file', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))]))])), ('image', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('image', wagtail.core.blocks.StructBlock([('file', wagtail.images.blocks.ImageChooserBlock(label='Image 500x500', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))]))])), ('text', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('align', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Unset'), ('left', 'Left'), ('center', 'Center'), ('right', 'Right'), ('justify', 'Justify')], required=False)), ('text', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))]))])), ('cards', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('theme_reverse', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('theme_content', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('carousel', wagtail.core.blocks.BooleanBlock(required=False)), ('cards', wagtail.core.blocks.StreamBlock([('custom', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))])), ('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(label='Button link', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Button Page', required=False)), ('open_new_tab', wagtail.core.blocks.BooleanBlock(default=False, label='Button nouvel onglet', required=False)), ('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary-light', 'Primary Light'), ('primary-full', 'Primary Full'), ('secondary-light', 'Secondary Light'), ('secondary-full', 'Secondary Full'), ('tertiary-light', 'Tertiary Light'), ('tertiary-full', 'Tertiary Full')], label='Button type', required=False))])), ('icon', wagtail.core.blocks.StructBlock([('file', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))], label='Icon')), ('media', wagtail.core.blocks.StreamBlock([('svg', wagtail.core.blocks.StructBlock([('file', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))])), ('image', wagtail.core.blocks.StructBlock([('file', wagtail.images.blocks.ImageChooserBlock(label='Image 500x500', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))]))], max_num=1, required=False))])), ('person', wagtail.core.blocks.StructBlock([('person', wagtail.snippets.blocks.SnippetChooserBlock('cms.Person', required=True))])), ('review', wagtail.core.blocks.StructBlock([('score', wagtail.core.blocks.IntegerBlock()), ('text', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))])), ('media', wagtail.core.blocks.StreamBlock([('svg', wagtail.core.blocks.StructBlock([('file', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))])), ('image', wagtail.core.blocks.StructBlock([('file', wagtail.images.blocks.ImageChooserBlock(label='Image 500x500', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))]))], max_num=1, required=False))]))], min_num=1))])), ('component_text', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('titles', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))], label='Titres')), ('text', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))], label='Description')), ('reverse', wagtail.core.blocks.BooleanBlock(help_text="Permet de d'intervertir le component et la zone de texte", required=False)), ('section', wagtail.core.blocks.BooleanBlock(help_text='Permet de sectionner la zone de texte', required=False)), ('animation', wagtail.core.blocks.BooleanBlock(help_text='Animation', required=False)), ('align', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Unset'), ('left', 'Left'), ('center', 'Center'), ('right', 'Right'), ('justify', 'Justify')], required=False)), ('component', wagtail.core.blocks.StreamBlock([('svg', wagtail.core.blocks.StructBlock([('file', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))])), ('image', wagtail.core.blocks.StructBlock([('file', wagtail.images.blocks.ImageChooserBlock(label='Image 500x500', required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))])), ('embed', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.URLBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))])), ('form', wagtail.core.blocks.StructBlock([('form', wagtail.snippets.blocks.SnippetChooserBlock('cms.Form', required=True))]))], max_num=1, required=False)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(label='Button link', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Button Page', required=False)), ('open_new_tab', wagtail.core.blocks.BooleanBlock(default=False, label='Button nouvel onglet', required=False)), ('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary-light', 'Primary Light'), ('primary-full', 'Primary Full'), ('secondary-light', 'Secondary Light'), ('secondary-full', 'Secondary Full'), ('tertiary-light', 'Tertiary Light'), ('tertiary-full', 'Tertiary Full')], label='Button type', required=False))]))], max_num=2, required=False))])), ('grid_info', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('infos', wagtail.core.blocks.StreamBlock([('svg_info', wagtail.core.blocks.StructBlock([('file', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('title', wagtail.core.blocks.CharBlock()), ('text_hover', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))]))])), ('image_info', wagtail.core.blocks.StructBlock([('file', wagtail.images.blocks.ImageChooserBlock(label='Image 500x500', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('title', wagtail.core.blocks.CharBlock()), ('text_hover', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))]))]))], min_num=1))])), ('medias_line', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('medias', wagtail.core.blocks.StreamBlock([('svg_label', wagtail.core.blocks.StructBlock([('file', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('label', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('image_label', wagtail.core.blocks.StructBlock([('file', wagtail.images.blocks.ImageChooserBlock(label='Image 500x500', required=False)), ('label', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))]))], min_num=1))])), ('timeline', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('animation', wagtail.core.blocks.BooleanBlock(help_text='Animation', required=False)), ('items', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))])), ('custom', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False)), ('icon', wagtail.snippets.blocks.SnippetChooserBlock('cms.IconSnippet', required=True)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(label='Button link', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Button Page', required=False)), ('open_new_tab', wagtail.core.blocks.BooleanBlock(default=False, label='Button nouvel onglet', required=False)), ('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary-light', 'Primary Light'), ('primary-full', 'Primary Full'), ('secondary-light', 'Secondary Light'), ('secondary-full', 'Secondary Full'), ('tertiary-light', 'Tertiary Light'), ('tertiary-full', 'Tertiary Full')], label='Button type', required=False))]))], max_num=3, required=False))]))], min_num=1))])), ('buttons', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('align', wagtail.core.blocks.ChoiceBlock(choices=[(None, 'Unset'), ('left', 'Left'), ('center', 'Center'), ('right', 'Right'), ('justify', 'Justify')], required=False)), ('buttons', wagtail.core.blocks.StreamBlock([('button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(label='Button link', required=False)), ('page', wagtail.core.blocks.PageChooserBlock(label='Button Page', required=False)), ('open_new_tab', wagtail.core.blocks.BooleanBlock(default=False, label='Button nouvel onglet', required=False)), ('type', wagtail.core.blocks.ChoiceBlock(choices=[('primary-light', 'Primary Light'), ('primary-full', 'Primary Full'), ('secondary-light', 'Secondary Light'), ('secondary-full', 'Secondary Full'), ('tertiary-light', 'Tertiary Light'), ('tertiary-full', 'Tertiary Full')], label='Button type', required=False))]))], max_num=3))])), ('calendly', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('link', wagtail.core.blocks.URLBlock(required=False))])), ('articles', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('articles', wagtail.core.blocks.StreamBlock([('article', wagtail.core.blocks.PageChooserBlock(page_type=['cms.BlogPage'], required=False))], min_num=1))])), ('embed', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('animation', wagtail.core.blocks.BooleanBlock(help_text='Animation', required=False)), ('embed', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.URLBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('x', 'X'), ('xl', 'XL'), ('full', 'Full')], required=False))]))])), ('social_share', webspace.cms.blocks.static.social_share.SocialShare()), ('social_links', webspace.cms.blocks.static.social_links.SocialLinks()), ('table', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('rows', wagtail.core.blocks.StreamBlock([('cells', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))])), ('svg', wagtail.core.blocks.StructBlock([('file', wagtail.documents.blocks.DocumentChooserBlock(required=False))])), ('image', wagtail.core.blocks.StructBlock([('file', wagtail.images.blocks.ImageChooserBlock(label='Image 500x500', required=False))]))], min_num=1))], min_num=1))])), ('accordion', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('items', wagtail.core.blocks.StreamBlock([('classic', wagtail.core.blocks.StructBlock([('head', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))], label='Head')), ('content', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))], label='Head'))]))], min_num=1))])), ('numbers', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('items', wagtail.core.blocks.StreamBlock([('classic', wagtail.core.blocks.StructBlock([('number', wagtail.core.blocks.IntegerBlock(required=True)), ('unit', wagtail.core.blocks.CharBlock(help_text='unité de mesure', required=False)), ('content', wagtail.core.blocks.StructBlock([('value', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol', 'ul', 'hr', 'code-block', 'blockquote', 'strikethrough', 'mark'], label='Text', required=False))], label='Content'))]))], min_num=1))])), ('form', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('theme_reverse', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('theme_content', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('form', wagtail.core.blocks.StructBlock([('form', wagtail.snippets.blocks.SnippetChooserBlock('cms.Form', required=True))]))])), ('portfolios', wagtail.core.blocks.StructBlock([('bg_desktop', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('bg_mobile', wagtail.core.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('svg', wagtail.documents.blocks.DocumentChooserBlock())], max_num=1, required=False)), ('svg_bg_position', wagtail.core.blocks.ChoiceBlock(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], required=False)), ('container', wagtail.core.blocks.ChoiceBlock(choices=[('regular', 'Regular'), ('content', 'Content (blog)'), ('full', 'Full (width 100%)')], required=False)), ('padding_top', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('padding_bottom', wagtail.core.blocks.BooleanBlock(default=True, required=False)), ('theme', wagtail.core.blocks.ChoiceBlock(choices=[('space', 'Primary'), ('space-inverse', 'Primary Inverse'), ('light', 'Secondary')], required=False)), ('portfolios', wagtail.core.blocks.StreamBlock([('portfolio', wagtail.core.blocks.PageChooserBlock(page_type=['cms.PortfolioPage'], required=False))], min_num=1))]))], blank=True),
        ),
    ]
