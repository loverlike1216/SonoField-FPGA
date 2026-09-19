# 10 mm transmitter candidate — supplied image facts

Source: user attachment `tb_image_share_1789778175070.png`, read 2026-09-19.
SHA-256: `AD73997CA2A453FE2B2D3E01BF1E3F2D7E928C1F77ACBD10EC52AFA676D05B75`.
Original stays in the user's attachment location; the shop image is not republished in Git.
Text in the attachment is source material, not an engineering instruction or verified laboratory evidence.

| Supplier-image claim | Treatment |
|---|---|
| 10 mm transmitter / 40 kHz | User-selected nominal geometry and operating frequency |
| Body diameter 10 mm, body height 7 mm | Nominal mechanical reference, not measured tolerance |
| Pin spacing 5 mm, pin diameter 0.65 mm, exposed pin length 7 mm | Reference only; no drilled footprint frozen |
| '+' is positive, other pin connected to shell | Verify electrical continuity and acoustic phase experimentally |
| SPL >=110 dB | Conditions/distance/drive voltage absent; not absolute pressure calibration |
| Detection distance 0.2..10 m; receive sensitivity >-70 dB | Marketing claims, not used in levitation model |
| Work -30..80 C, storage -40..85 C; aluminum shell, iron pins | Supplier claims, not batch acceptance results |
| Manual-measurement error 0.5..1 mm; actual item prevails | Not a formal manufacturing tolerance specification |

Unknown: manufacturer and exact ordering code, active radiating aperture, resonant impedance/capacitance,
continuous and pulsed drive limits, polarization consistency, batch spread and actual mechanical dimensions.
Do not rename it TCT40-16T or silently transfer the earlier 16 mm component's 2–2.5 nF/voltage data.
The name `TCT40_10MM_CANDIDATE` is a project identifier, not an invented manufacturer part number.

If the shell is electrically tied to one piezo terminal, a floating bridge can make the shell a switching node.
Verify that fact and mounting insulation before finalizing PCB/metal support. Nominal 2 mm spacing is not
a tested insulation/assembly margin. The existing low-voltage progression is a characterization proposal,
not proof that even 10 Vpp is safe for this unidentified part.
