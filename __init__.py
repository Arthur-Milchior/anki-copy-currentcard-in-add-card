from aqt import gui_hooks, mw
from aqt.addcards import AddCards

def init(add_cards):
    editor = add_cards.editor
    note = editor.note
    if note is None:
        return
    if mw.state != "review":
        return
    reviewer = mw.reviewer
    current_card = reviewer.card
    if current_card is None:
        return

    current_note = current_card.note()
    editor.note.tags = current_note.tags
    showInfo(" ".join(current_note.tags))
    current_did = current_card.odid or current_card.did
    add_cards.deckChooser.selected_deck_id = current_did

    # didn't found other way to update tags, as editor.updateTags() throws error
    mw.reset()

gui_hooks.add_cards_did_init.append(init)
