"""Candidate schematic connectivity; physical timing/safety/BOM gates stay open."""
import json
from tx_design import OUT


class Sheet:
    def __init__(self,name,notes):
        self.name=name;self.notes=[name+' | DRAFT - NOT FOR FABRICATION']+notes;self.parts=[]

    def part(self,key,ref,x,y,nets,value=None,generic=False,dnp=False):
        self.parts.append(dict(key=key,ref=ref,value=value or key,x=x,y=y,
            nets={str(k):(v.upper() if v else None) for k,v in nets.items()},generic=generic,dnp=dnp))

    def passive(self,key,ref,value,x,y,a,b,dnp=False):
        self.part(key,ref,x,y,{1:a,2:b},value,True,dnp)

    def cap(self,ref,x,y,power,ground,value='100nF X7R'):
        self.passive('C',ref,value,x,y,power,ground)

    def record(self):return vars(self)


def build():
    sheets=[]
    def page(name,notes):
        s=Sheet(name,notes);sheets.append(s);return s
    for b,offset in [('U',0),('L',16)]:
        v,g=f'3V3_{b}',f'DGND_{b}'
        for group in range(4):
            s=page(f'SERIALIZER_{b}_{group}',[
                'Four outputs per lane: QA/QB/QC/QD = channel 4L + 0/1/2/3.',
                'Shift bit3 first, bit0 last. 66 MHz physical timing remains B04 OPEN.',
                'Clock/latch branch serves four 595 devices; /OE default disable upstream.'])
            for j in range(4):
                local=group*4+j;lane=offset+local;x=260+500*(j%2);y=590-300*(j//2)
                n={1:f'{b}_TX{4*local+1:02d}_IN',2:f'{b}_TX{4*local+2:02d}_IN',3:f'{b}_TX{4*local+3:02d}_IN',
                   4:None,5:None,6:None,7:None,8:g,9:None,10:v,11:f'{b}_SCLK{group}',12:f'{b}_LATCH{group}',
                   13:f'{b}_OE_N',14:f'{b}_SER{local:02d}',15:f'{b}_TX{4*local:02d}_IN',16:v}
                s.part('SN74LVC595APWR',f'U_SER{lane:02d}',x,y,n)
                s.cap(f'C_SER{lane:02d}',x+20,y+110,v,g)
        s=page(f'CLOCK_ENABLE_{b}',[
            'Clock-only LVC244 delay has unclosed hold timing; do not freeze B04.',
            'KILL is pulled high. Independent watchdog/power qualification is OPEN.',
            '33R series clock resistors are tuning candidates, not measured termination.'])
        n={1:g,10:g,19:g,20:v}
        for i,(inp,out) in enumerate(zip([2,4,6,8,11,13,15,17],[18,16,14,12,9,7,5,3])):
            n[inp]=f'{b}_shift_clock' if i<4 else f'{b}_latch_clock'
            n[out]=f'{b}_CLK_RAW{i}'
        s.part('SN74LVC244APWR',f'U_CLK_{b}',270,530,n)
        s.part('SN74LVC1G32DBVR',f'U_DISABLE_{b}',780,600,
               {1:f'{b}_output_disable',2:f'{b}_KILL',3:g,4:f'{b}_OE_N',5:v})
        s.cap(f'C_CLK_{b}',240,690,v,g);s.cap(f'C_DISABLE_{b}',780,690,v,g)
        s.passive('R',f'R_KILL_{b}','10k',780,480,v,f'{b}_KILL')
        s.passive('R',f'R_DISABLE_{b}','10k',780,410,v,f'{b}_output_disable')
        for i in range(8):
            s.passive('R',f'R_CLK_{b}{i}','33R TUNE',240+270*(i%3),300-65*(i//3),
                f'{b}_CLK_RAW{i}',f'{b}_SCLK{i}' if i<4 else f'{b}_LATCH{i-4}')
        for group in range(3):
            s=page(f'LEVEL_TX_{b}_{group}',[
                'VCCA = verified FPGA bank VCCO (TBD); VCCB = local 3.3 V.',
                'Both DIR pins high for A-to-B. LEVEL_OE_N pulled high: default disconnected.',
                'LEVEL_OE_N must be qualified by board configuration/power policy (OPEN).'])
            n={1:'VCCO_FPGA',2:'VCCO_FPGA',11:'VCCO_FPGA',12:g,13:g,22:'LEVEL_OE_N',23:v,24:v}
            for i in range(8):
                if group<2: a=f'serial_data[{offset+8*group+i}]';out=f'{b}_SER{8*group+i:02d}'
                elif i<4:
                    a=['shift_clock','latch_clock','output_disable',f'rx_blank[{0 if b=="U" else 1}]'][i]
                    out=[f'{b}_shift_clock',f'{b}_latch_clock',f'{b}_output_disable',f'{b}_rx_blank'][i]
                else:a=g;out=None
                n[3+i]=a;n[21-i]=out
            tag=f'{b}{group}'
            s.part('SN74AXC8T245PWR',f'U_LEVEL_{tag}',430,510,n)
            s.cap(f'C_LEVEL_A_{tag}',220,690,'VCCO_FPGA',g);s.cap(f'C_LEVEL_B_{tag}',780,690,v,g)
            if b=='U' and group==0:s.passive('R','R_LEVEL_OE','100k',750,350,'VCCO_FPGA','LEVEL_OE_N')
    # ADC control and return translators have separate, fixed direction groups.
    for side in ['CONTROL','RETURN']:
        s=page(f'LEVEL_ADC_{side}', ['FPGA-side voltage remains B03 TBD. ADC-side logic is 3.3 V.',
            'Preserve source-synchronous DOUT timing; no independent bit synchronizers.'])
        n={1:'VCCO_FPGA',2:'VCCO_FPGA' if side=='CONTROL' else 'DGND_A',11:'VCCO_FPGA' if side=='CONTROL' else 'DGND_A',
           12:'DGND_A',13:'DGND_A',22:'LEVEL_OE_N',23:'3V3_A',24:'3V3_A'}
        sigs=['adc_reset','adc_convst','adc_cs_n','adc_sclk','adc_sdi'] if side=='CONTROL' else ['adc_busy']+[f'adc_dout[{i}]' for i in range(4)]
        for i in range(8):
            n[3+i]=sigs[i] if i<5 else ('DGND_A' if side=='CONTROL' else None)
            n[21-i]='ADC_'+sigs[i] if i<5 else (None if side=='CONTROL' else 'DGND_A')
        s.part('SN74AXC8T245PWR',f'U_LEVEL_ADC_{side}',430,510,n)
        s.cap(f'C_LEVEL_ADC_{side}_A',200,690,'VCCO_FPGA','DGND_A');s.cap(f'C_LEVEL_ADC_{side}_B',780,690,'3V3_A','DGND_A')
    s=page('ADC_AD7606B',[
        'OS=111, PAR/SER=1: software serial mode; internal reference enabled.',
        '4 DOUT lanes; 32 SCLK/frame. Source/return timing and startup power-good OPEN.',
        'REFCAP A+B share 10uF; REGCAP nodes remain separate. Unused parallel inputs tied low.'])
    g='AGND_A';v='5VA_A';d='3V3_A'
    n={1:v,2:g,3:d,4:d,5:d,6:d,7:d,8:g,9:'ADC_adc_convst',10:d,11:'ADC_adc_reset',12:'ADC_adc_sclk',13:'ADC_adc_cs_n',
       14:'ADC_adc_busy',15:'ADC_FRSTDATA',23:d,24:'ADC_adc_dout[0]',25:'ADC_adc_dout[1]',26:g,27:'ADC_adc_dout[2]',28:'ADC_adc_dout[3]',
       29:'ADC_adc_sdi',34:d,35:g,36:'ADC_REGCAP1',37:v,38:v,39:'ADC_REGCAP2',40:g,41:g,42:'ADC_REFOUT',43:g,44:'ADC_REFCAP',45:'ADC_REFCAP',46:g,47:g,48:v}
    for pin in list(range(16,23))+list(range(30,34)):n[pin]=g
    for i in range(8):n[49+2*i]=f'ADC_IN{i}';n[50+2*i]=g
    s.part('AD7606BBSTZ','U_ADC',530,465,n)
    for i,(rail,val) in enumerate([('ADC_REGCAP1','1uF'),('ADC_REGCAP2','1uF'),('ADC_REFCAP','10uF'),('ADC_REFOUT','100nF')]):
        s.cap(f'C_ADC_REF{i}',180,610-100*i,rail,g,val)
    for i,pin in enumerate([1,37,38,48]):s.cap(f'C_ADC_AV{pin}',920,630-90*i,v,g)
    s.cap('C_ADC_DV',920,230,d,g);s.cap('C_ADC_BULK',530,120,v,g,'10uF')
    s.part('TP','TP_ADC_FRSTDATA',180,170,{1:'ADC_FRSTDATA'},'FRSTDATA',True)
    for b,offset in [('U',0),('L',4)]:
        v,g,ref=f'5VA_{b}',f'AGND_{b}',f'VREF_{b}'
        s=page(f'REFERENCE_{b}', ['REF5025 external AFE bias; ADC retains its own internal reference.',
                'DNC pins unconnected. Reference noise, buffering/load and bypass require review.'])
        s.part('REF5025AIDR',f'U_REF_{b}',450,540,{1:None,2:v,3:None,4:g,5:f'REF_NR_{b}',6:ref,7:None,8:None})
        s.cap(f'C_REF_IN_{b}',200,690,v,g,'1uF');s.cap(f'C_REF_OUT_{b}',800,690,ref,g,'10uF')
        s.cap(f'C_REF_NR_{b}',450,300,f'REF_NR_{b}',g,'1uF')
        s=page(f'RX_BLANK_{b}', ['SEL low = AFE, high = 2.5 V bias. 100k pull-up defaults to blank.',
            'Switch is downstream of AFE; amplifier overload/recovery NOT protected by this switch.',
            '47R + 1nF ADC input filters; actual settling and phase must be measured.'])
        n={1:f'{b}_rx_blank',8:g,15:g,16:v}
        for i,(a,bpin,out) in enumerate([(2,3,4),(5,6,7),(11,10,9),(14,13,12)]):n[a]=f'{b}_RX{i}_FILT';n[bpin]=ref;n[out]=f'{b}_RX{i}_MUX'
        s.part('TMUX1574PWR',f'U_BLANK_{b}',350,570,n)
        s.cap(f'C_BLANK_{b}',250,690,v,g);s.passive('R',f'R_BLANK_{b}','100k',750,660,f'3V3_{b}',f'{b}_rx_blank')
        for i in range(4):
            s.passive('R',f'R_ADC_{b}{i}','47R',270+500*(i%2),330-140*(i//2),f'{b}_RX{i}_MUX',f'ADC_IN{offset+i}')
            s.cap(f'C_ADC_IN{offset+i}',400+500*(i%2),280-140*(i//2),f'ADC_IN{offset+i}','AGND_A','1nF C0G')
        for pair in range(2):
            s=page(f'AFE_{b}_{pair}', ['OPA4192 two stages per RX: G1=11, G2=2, total nominal22.',
                '10nF coupling / 100k bias. DNP bypass mutually exclusive with stage2 selection.',
                'BAT54S substitution/protection capacitance, overload and complex gain require qualification.'])
            first=2*pair
            op={4:v,11:g}
            # Each signal consumes two op-amps; quad order A/B then C/D.
            for j in range(2):
                ch=first+j;tag=f'{b}{ch}';y=610-285*j
                raw=f'{b}_RX{ch}_RAW';protected=f'{b}_RX{ch}_PROT';bias=f'{b}_RX{ch}_BIAS'
                one=f'{b}_RX{ch}_G1';two=f'{b}_RX{ch}_G2';sel=f'{b}_RX{ch}_SEL';neg1=f'{b}_RX{ch}_N1';neg2=f'{b}_RX{ch}_N2'
                out1,minus1,plus1,out2,minus2,plus2=(1,2,3,7,6,5) if j==0 else (8,9,10,14,13,12)
                op.update({out1:one,minus1:neg1,plus1:bias,out2:two,minus2:neg2,plus2:one})
                s.part('RX',f'{"UPPER" if b=="U" else "LOWER"}_RX{ch}',150,y,{1:g,2:raw},'TCT40-10R1 / MPN_TBD',True)
                s.passive('R',f'R_PROT_{tag}','1k',350,y,raw,protected)
                s.part('BAT54S',f'D_PROT_{tag}',600,y,{1:g,2:v,3:protected},'BAT54S / SUBSTITUTE_REVIEW')
                s.passive('C',f'C_AC_{tag}','10nF C0G',880,y,protected,bias)
                s.passive('R',f'R_BIAS_{tag}','100k',900,y-70,bias,ref)
                for k,(val,a,z) in enumerate([('100k 0.1%',one,neg1),('10k 0.1%',neg1,ref),('10k 0.1%',two,neg2),('10k 0.1%',neg2,ref)]):
                    s.passive('R',f'R_GAIN_{tag}_{k}',val,150+230*k,y-140,a,z)
                s.passive('R',f'R_SEL_{tag}','0R FIT G22',150,y-210,two,sel)
                s.passive('R',f'R_BYPASS_{tag}','0R DNP G11',390,y-210,one,sel,True)
                s.passive('R',f'R_LP_{tag}','1k',650,y-210,sel,f'{b}_RX{ch}_FILT')
                s.cap(f'C_LP_{tag}',900,y-210,f'{b}_RX{ch}_FILT',g,'1nF C0G')
            # Amplifier on its own linked sheet to keep the gain-network sheets readable.
            a=page(f'AFE_AMP_{b}_{pair}', ['One OPA4192 quad serves two RX channels; feedback/bias networks on matching AFE sheet.',
                       '5 V single supply; V- is AGND. No guaranteed overload recovery.'])
            a.part('OPA4192IPWR',f'U_AFE_{b}{pair}',500,500,op)
            a.cap(f'C_AFE_{b}{pair}',220,690,v,g);a.cap(f'C_AFE_BULK_{b}{pair}',820,690,v,g,'1uF')
    return {'status':'DRAFT_NOT_FOR_FABRICATION','sheets':[s.record() for s in sheets]}


if __name__=='__main__':
    design=build();refs=[p['ref'] for s in design['sheets'] for p in s['parts']]
    assert len(refs)==len(set(refs))
    (OUT/'project/system_design.json').write_text(json.dumps(design,indent=2)+'\n',encoding='utf-8')
    print(len(design['sheets']),'system sheets;',len(refs),'components')
