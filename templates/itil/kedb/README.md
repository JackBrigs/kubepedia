# KEDB — Known Error Database (сгенерировано из troubleshooting-слоя базы)

ITIL 4 Known Error records, отрендеренные из базы знаний. **Не редактировать руками** —
перегенерируется `scripts/gen_kedb.py`. Формат: симптом / затронутые CIs / root cause /
workaround-fix / источник. Внутренних KDS-ID нет (пользовательский деливерабл).


**Всего: 223 Known Error записей.**

## Домены

- [etcd & control-plane](etcd-control-plane.md) — 37 записей
- [storage](storage.md) — 20 записей
- [dns](dns.md) — 5 записей
- [networking & CNI](networking-cni.md) — 45 записей
- [security & admission](security-admission.md) — 30 записей
- [node & runtime](node-runtime.md) — 25 записей
- [scaling](scaling.md) — 2 записей
- [upgrade & join](upgrade-join.md) — 11 записей
- [addons](addons.md) — 13 записей
- [other](other.md) — 35 записей
