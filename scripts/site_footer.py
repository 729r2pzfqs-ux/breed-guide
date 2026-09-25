"""Standard site footer (one per language). Used by the footer/404/privacy
maintenance passes so every page type shares the same links."""

LABELS = {
    'en': ('Browse Breeds', 'Breed Quiz', 'Compare', 'Guides', 'FAQ', 'About', 'Privacy', 'Contact'),
    'es': ('Explorar razas', 'Test de razas', 'Comparar', 'Guías', 'Preguntas frecuentes', 'Acerca de', 'Privacidad', 'Contacto'),
    'de': ('Rassen entdecken', 'Rassen-Quiz', 'Vergleichen', 'Ratgeber', 'FAQ', 'Über uns', 'Datenschutz', 'Kontakt'),
    'fr': ('Parcourir les races', 'Quiz des races', 'Comparer', 'Guides', 'FAQ', 'À propos', 'Confidentialité', 'Contact'),
    'it': ('Esplora le razze', 'Quiz razze', 'Confronta', 'Guide', 'FAQ', 'Chi siamo', 'Privacy', 'Contatti'),
    'pt': ('Explorar raças', 'Quiz de raças', 'Comparar', 'Guias', 'Perguntas frequentes', 'Sobre', 'Privacidade', 'Contato'),
    'fi': ('Selaa rotuja', 'Rotutesti', 'Vertaile', 'Oppaat', 'UKK', 'Tietoa meistä', 'Tietosuoja', 'Yhteystiedot'),
    'sv': ('Utforska raser', 'Rasquiz', 'Jämför', 'Guider', 'Vanliga frågor', 'Om oss', 'Integritet', 'Kontakt'),
    'nl': ('Rassen bekijken', 'Rassenquiz', 'Vergelijken', 'Gidsen', 'FAQ', 'Over ons', 'Privacy', 'Contact'),
    'da': ('Udforsk racer', 'Racequiz', 'Sammenlign', 'Guides', 'FAQ', 'Om os', 'Privatliv', 'Kontakt'),
    'ja': ('犬種一覧', '犬種診断', '比較', 'ガイド', 'よくある質問', '運営者情報', 'プライバシー', 'お問い合わせ'),
    'no': ('Utforsk raser', 'Rasequiz', 'Sammenlign', 'Guider', 'Vanlige spørsmål', 'Om oss', 'Personvern', 'Kontakt'),
    'pl': ('Przeglądaj rasy', 'Quiz ras', 'Porównaj', 'Poradniki', 'FAQ', 'O nas', 'Prywatność', 'Kontakt'),
    'ru': ('Все породы', 'Тест пород', 'Сравнить', 'Статьи', 'Вопросы и ответы', 'О нас', 'Конфиденциальность', 'Контакты'),
    'tr': ('Irkları keşfet', 'Irk testi', 'Karşılaştır', 'Rehberler', 'SSS', 'Hakkımızda', 'Gizlilik', 'İletişim'),
    'zh': ('浏览犬种', '犬种测验', '比较', '指南', '常见问题', '关于我们', '隐私政策', '联系我们'),
}


def footer(lang):
    p = '' if lang == 'en' else '/' + lang
    b, q, c, g, faq, about, priv, contact = LABELS[lang]
    links = [(p + '/search/', b), (p + '/quiz/', q), (p + '/compare/', c), (p + '/articles/', g),
             (p + '/faq/', faq), (p + '/about/', about), ('/privacy/', priv)]
    items = '\n'.join(f'                    <a href="{h}" class="hover:text-white transition">{t}</a>' for h, t in links)
    return f'''<footer class="bg-emerald-900 py-12 px-4 mt-12">
        <div class="max-w-5xl mx-auto">
            <div class="flex flex-col md:flex-row items-center justify-between gap-6">
                <a href="{p}/" class="flex items-center gap-3">
                    <img src="/logo-192-green.png" alt="BreedFinder" width="40" height="40" loading="lazy" class="h-10 w-10 brightness-0 invert">
                    <span class="text-xl font-bold text-white">BreedFinder</span>
                </a>
                <nav aria-label="Footer" class="flex flex-wrap justify-center gap-x-6 gap-y-2 text-sm text-emerald-200">
{items}
                </nav>
            </div>
            <div class="mt-8 pt-8 border-t border-emerald-800 text-center text-sm text-emerald-200">
                <p>&copy; 2026 BreedFinder &middot; {contact}: <a href="mailto:info@breedfinder.org" class="hover:text-white transition">info@breedfinder.org</a></p>
            </div>
        </div>
    </footer>'''
